import glob, sys, os

video_path = sys.argv[1]
for file in glob.glob("{}/*".format(video_path)):
    print(file)
    os.system("yolo detect predict model=best_shoplifting.pt save=True source={}".format(file))