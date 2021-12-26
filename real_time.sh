#!/bin/sh

# configure
TARGET_ARCH_ABI=armv7hf # for Raspberry Pi 3B
PADDLE_LITE_DIR=./Paddle-Lite
if [ "x$1" != "x" ]; then
    TARGET_ARCH_ABI=$1
fi

# build
rm -rf build
mkdir build
cd build
cmake -DPADDLE_LITE_DIR=${PADDLE_LITE_DIR} -DTARGET_ARCH_ABI=${TARGET_ARCH_ABI} ..
make

# run
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${PADDLE_LITE_DIR}/libs/${TARGET_ARCH_ABI} ./fatigueDriving ../models/ssd_lite/model.nb ../labels/pascalvoc_label_list
