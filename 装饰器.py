import  time
def index():
    time.sleep(2)


start_time=time.time()

index()
end_time=time.time()
print(end_time-start_time)