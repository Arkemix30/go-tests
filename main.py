from piramid_prim_test.piramid_task import piramid_prim
from redis_test.redis_task import run_redis_task

def main():
    print("PIRAMID PRIM TASK")
    print("\nPiramid with 8:")
    piramid_prim(8)
    print("\nPiramid with 5:")
    piramid_prim(5)

    print("\nREDIS MERGE TASK")
    run_redis_task()

if __name__ == "__main__":
    main()