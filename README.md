# test / dev

# run image 
 ./build.sh
 ./run.sh

# run localy (test)
 uv run test_train.py
 uv run test_query.py
  image read
  The image has dimensions 768x768 and 3 channels.
  
  image 1/1 C:\git\a\com-areal-imagery\data\ship\test\images\02e39612d_jpg.rf.cc5483bb711f080d12b644ff62cf977a.jpg: 768x768 1 ship, 1219.1ms
  Speed: 5.3ms preprocess, 1219.1ms inference, 12.8ms postprocess per image at shape (1, 3, 768, 768)
  is a list
  [
    {
      "name": "ship",
      "class": 0,
      "confidence": 0.61581,
      "box": {
        "x1": 97.41543,
        "y1": 554.42657,
        "x2": 336.60062,
        "y2": 680.40387
      }
    }
  ]
  finished

# get image 
podman pull heartexlabs/label-studio:20250522.103436-ls-release-1-19-0-3d6e6771c
label-studio start --username <username> --password <password> [--user-token <token-at-least-5-chars>]

# run label studio
do nor mount windows filesystems directly - it's may fail with chmod errors
 podman run -it -p 8080:8080 -v labelstudio_flags:/label-studio/data  heartexlabs/label-studio:latest

# build train image
 podman build  -f Dockerfile.train.flags . -t flags_train:dev0.1

# run train image
 podman run -v ./dataset/XX/XX:/dataset/  flags_train:dev0.1

# query
 uv run test_flag_query.py 

 for FILE in  datasets/Terrorflags/images_raw/*jpg ; do curl -X POST -F "image=@$FILE" http://localhost:5000/predict; done 

# build query
 podman build -f Dockerfile.dedect.flags . -t flags-dedect-cuda124:dev0.1
 podman run  -e YOLO_MODEL="/app/flags.pt" trieder83/yolo-dedect:dev0.1cpu


# cuda test
$ uv run gputest.py
CUDA Available: True
Device: NVIDIA GeForce RTX 3050 Laptop GPU
