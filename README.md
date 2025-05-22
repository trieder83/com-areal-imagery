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


# run label studio
do nor mount windows filesystems directly - it's may fail with chmod errors
 podman run -it -p 8080:8080 -v labelstudio_flags:/label-studio/data  heartexlabs/label-studio:latest


# build train image
 docker build  -f Dockerfile.train.flags . -t flags_train
