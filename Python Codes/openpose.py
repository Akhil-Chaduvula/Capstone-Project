# download and install the latest version of cmake
! wget -c "https://github.com/Kitware/CMake/releases/download/v3.14.4/cmake-3.14.4.tar.gz"
! tar xf cmake-3.14.4.tar.gz
! cd cmake-3.14.4 && ./configure && make && sudo make install

# download OpenPose from Git Repository
! git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git

# install dependencies
! cd openpose/scripts/ubuntu && bash ./install_deps.sh && bash ./install_cuda.sh && bash ./install_cudnn.sh
! apt install -y cmake sudo libopencv-dev

# this is just a fix to address few compilation issues
! sed -i 's/execute_process(COMMAND git checkout master WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}\/3rdparty\/caffe)/execute_process(COMMAND git checkout f019d0dfe86f49d1140961f8c7dec22130c83154 WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}\/3rdparty\/caffe)/g' openpose/CMakeLists.txt

! cd openpose && git pull origin master 

# now the important step - compiling OpenPose with cmake
! /bin/rm -r openpose/build
! cd openpose && mkdir build && cd build && cmake .. && make -j `nproc`

! cd openpose && ./build/examples/openpose/openpose.bin --video '/content/gdrive/MyDrive/Capstone/Video.MOV' --display 0 --disable_blending --face --hand --write_video '/content/gdrive/MyDrive/Capstone/OpenPose_Video.avi'
