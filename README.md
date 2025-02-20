# hifilter
simple image filter

### DCT-NET
* cd hifilter/thirdparty/
* git clone https://github.com/menyifang/DCT-Net ( git clone https://gitee.com/last911/DCT-Net.git )
* pip install opencv-python tensorflow easydict modelscope addict
* modelscope download iic/cv_unet_person-image-cartoon_compound-models --local_dir ./models/cv_unet_person-image-cartoon_compound-models
* rm -rf ./hifilter/thirdparty/DCT-Net/assets
