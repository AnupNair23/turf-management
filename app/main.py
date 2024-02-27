from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import pitch
from app.core.config import settings
from app.cron.update_weather import update_pitch_values
from app.db.database import connect_to_mongo, close_mongo_connection
import schedule
import threading
import time
   
app = FastAPI(
    title="Pitch Management System",
    description="A REST API for monitoring pitch health.",
    version="1.0.0",
)
# Set up Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router from endpoints
app.include_router(pitch.router, prefix="/pitches", tags=["pitches"])
# app.include_router(weather.router, prefix="/weather", tags=["weather"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Pitch Management System API!"}

# Possibly more application event handlers like startup and shutdown
async def startup_event():
    # Initialize database connection or any other startup tasks
    connect_to_mongo
    schedule_cron_job()
    pass

async def shutdown_event():
    close_mongo_connection
    # Cleanup tasks, like closing database connections
    pass


def schedule_cron_job():
    # Schedule the function to run every six hours
    schedule.every().minute.do(update_pitch_values)

    # Run the scheduler in a separate thread
    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)  # Sleep for 1 second to avoid consuming too much CPU

    # Start the scheduler thread
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()