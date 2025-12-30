import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler  # type: ignore[import-untyped]

from src.config.settings import settings

logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)


async def collect_and_report():
    """Main job: collect yields and send Telegram report."""
    logger.info("Starting yield collection...")
    # TODO: Implement collection logic
    # TODO: Save to CSV
    # TODO: Send Telegram report
    logger.info("Collection complete")


def main():
    scheduler = AsyncIOScheduler(timezone=settings.scheduler_timezone)
    scheduler.add_job(
        collect_and_report,
        "interval",
        hours=settings.scheduler_interval_hours,
        id="yield_collection",
    )

    scheduler.add_job(collect_and_report, "date", id="initial_run")

    scheduler.start()
    logger.info(f"Scheduler started. Running every {settings.scheduler_interval_hours} hour(s)")

    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Shutting down...")


if __name__ == "__main__":
    main()
