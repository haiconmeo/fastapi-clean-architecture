from multiprocessing import cpu_count
import uvicorn

num_workers = cpu_count()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=4545, reload=True, log_level="debug"
                )
