
# tf-stitch
Starter code with best practices for different Deep Learning problems in one command.

This Package provides Tensorflow 2.0 boilerplate code , for deep learning problem domains.

To install, in command line enter -

    pip install tf-stitch
 
View Pypi project on [https://pypi.org/project/tf-stitch/](https://pypi.org/project/tf-stitch/)

## Why use this?
**If you have been working in deep learning or have just started, you will find yourself writing the same imports, same training loop, same data fetching commands, same model declaration every time.**

Personally, found myself copy-pasting MNIST models to get started with a project.
And Even copy-pasting does not work as there are many parts of deep learning code that are needed in different combinations for different problems.

This Package is created just to solve this problem for our most beloved framework Tensorflow 2.0.
Deep learning is an exciting field full of awesome ideas and new concepts popping every day. 
**Custom stitched boiler code lets you focus on the uniqueness of your implementation and not the repetitive code**.

**Keras and Tensorflow 2.0, because of simple API, allows you to implement many ideas in less time. This Package just aims to double(2X) that efficiency.**

## USAGE

    usage: tf-stitch output_file [-d DOMAIN]
    [--dataset DATASET] [--model MODEL] [--training TRAINING]
    [--testing TESTING]

Example -

    tf-stitch output_script.py -d=vision
or 
    
    tf-stitch output_notebook.ipynb -d=nlp

Here `output_script.py` and `output_notebook.ipynb`  are  the generated output files with starter code.
`output_file` is required for command to run. 
File can have extension .py or .ipynb for generating python script or jupyter notebook.

**Arguments:**
  
**-d , --domain DOMAIN**
Domain problem type for selecting appropriate model
and dataset. See `tf_stitch/template.json` for default datasets and model for each domain option.
Current domain options are -

 - vision
 - nlp
 - structured

**Either provide domain argument or dataset and model arguments** 

**- dataset DATASET**  :  Select any of Tensorflow datasets. See [catalog](https://www.tensorflow.org/datasets/catalog/overview).
**--model MODEL**   :     Select a Deep Learning Model
Current available options -

 - conv - Convolution model
 - rnn - GRU sequence model
 - dnn - Fully connected network
 - custom - Custom layer network

**--training TRAINING**  : Type of training loop.
Options -
 - custom 
 - built-in

**--testing TESTING**  :   If to include testing, True or False

Example -

    tf-stitch output.ipynb --dataset = cifar100 --model = conv 
    --training = custom --testing = True

**All the templates are in their respective folder in `tf_stitch/templates` . Feel free to change templates according to your taste and also submit a pull request if it can be helpful for others as well.**


## Contributing
Hey There, this project requires your feedback and contribution to improve.
You can contribute, but not restricted to, in following ways -

 - **Providing Feedback and submitting feature request.**
 - **Apply best and latest TF2.0 practices.**
 - **Add more template and domain options.**

Looking forward to hear from you : )
