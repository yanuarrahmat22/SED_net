{% load static %}
<script async src="//jsfiddle.net/bootstrapious/8w7a50n2embed/"></script>
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Welcome to SED.net</title>
    <style>
        #upload {
            opacity: 0;
        }

        #upload-label {
            position: absolute;
            top: 50%;
            left: 1rem;
            transform: translateY(-50%);
        }

        .image-area {
            border: 2px dashed rgba(255, 255, 255, 0.7);
            padding: 1rem;
            position: relative;
        }

        .image-area::before {
            content: 'Uploaded image result';
            color: #fff;
            font-weight: bold;
            text-transform: uppercase;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 0.8rem;
            z-index: 1;
        }

        .navbar {
            background-color: #01DEE0;
        }

        .image-area img {
            z-index: 2;
            position: relative;
        }

        body {
            min-height: 100vh;
            background-color: #757f9a;
            background-image: linear-gradient(147deg, #757f9a 0%, #d7dde8 100%);
        }
    </style>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">

</head>

<body>
    <nav class="navbar navbar-custom">
        <div class="container-fluid">
            <a class="navbar-brand" href="home"><img style="height:30px" src="{% static 'img/sedlogo.png' %}" alt="My image"></a>
            <!-- <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button> -->
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">

                </ul>
            </div>
        </div>
    </nav>
    <div class="container py-5">

        <header class="text-white text-center">
            <h1 class="display-4">Student Engagement Detection</h1>
            <h5 class="display-6">based on facial expressions</h5>
        </header>


        <div class="row py-4">
            <div class="    mx-auto">

                <!-- Upload image input-->
                <form method="post" enctype="multipart/form-data" action="reupload_images">

                    {% csrf_token %}
                    <div class="d-grid gap-2 col-6 mx-auto">
                        <button type="submit" class="btn btn-info" type="button">RE-UPLOAD IMAGE</button>
                    </div>
                </form>
                <div class="block"></div>
                <!-- Uploaded image area-->
                <form method="post" enctype="multipart/form-data" action="predict_image">
                    {% csrf_token %}
                    <div class="d-grid gap-2 col-6 mx-auto">
                        <button type="submit" class="btn btn-info" type="button">PREDICT IMAGE</button>
                    </div><br>
                    <div class="mb-3">
                        <p class="font-italic text-white text-center">The image uploaded will be rendered inside the box below.</p>
                        {% for imgs in images %}
                            {% if forloop.last %}
                                <div class="image-area mt-4"><img id="imageResult" src="{{ imgs.name_Img.url }}" alt="" class="img-fluid rounded shadow-sm mx-auto d-block"></div>
                            {% endif %}
                        {% endfor %}
                    </div>
                </form>

            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-W8fXfP3gkOKtndU4JGtKDvXbO53Wy8SZCQHczT5FMiiqmQfUpWbYdTil/SxwZgAN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.min.js" integrity="sha384-skAcpIdS7UcVUC05LJ9Dxay8AXcDYfBJqt1CJ85S/CFujBsIzCIv+l9liuYLaMQ/" crossorigin="anonymous"></script>
</body>

</html>