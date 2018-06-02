args = {'--content_image':None,
        '--style_image':None,
        '--content_weight':1,
        '--style_weight':1e4,
        '--style_imgs_weights':[1.0],
        '--style_layer_weights':[0.2,0.2,0.2,0.2,0.2],
        '--content_layer_weights':[0.2],
        '--original_colors':False,
        '--color_convert_type':'yuv',
        '--pooling_type':'avg',
        '--device':'/cpu:0',
        '--optimizer':'lbfgs',
        '--learning_rate':1,
        '--max_iterations':1000,
        '--content_loss_function':1,
        '--max_size':512
        }