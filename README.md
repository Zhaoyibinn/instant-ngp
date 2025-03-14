python scripts/colmap2nerf.py --out data/colmap_scan24/transforms.json --images data/colmap_scan24/images/ --text data/colmap_scan24/sparse/0/

python ./scripts/run.py --mode nerf --scene ./transforms.json  --save_mesh ./output/DTU.ply --n_steps 10000 --gui


# 编译
export CC=/usr/bin/gcc-11

export CXX=/usr/bin/g++-11

cmake . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_CUDA_COMPILER="/usr/local/cuda-11.8/bin/nvcc"

cmake --build build --config RelWithDebInfo -j8

关于LIBCXX报错可以参考[LIBCXX](https://blog.csdn.net/weixin_46124467/article/details/144040873)

sudo rm /home/zhaoyibin/anaconda3/envs/ngp/lib/libstdc++.so.6

ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /home/zhaoyibin/anaconda3/envs/ngp/lib/libstdc++.so.6