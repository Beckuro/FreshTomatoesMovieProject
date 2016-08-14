import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap 3 -->
    <meta name="description" content="">
    <meta name="author" content="">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/css/bootstrap.min.css">

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="http://getbootstrap.com/assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <!--
    <link href="sticky-footer-navbar.css" rel="stylesheet">
    -->

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        html {
          position: relative;
          min-height: 100%;
        }
        body {
           margin-bottom: 60px;
           padding: 0;
           font-family: sans-serif;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        .jumbotron {
          padding-left = 10px;
          margin: 10px 5px 2px 3px;
        }

        h3 {
          text-align: center;
        }

        .text-media {
          margin-top: 10px;
          margin-left: 10px;
          padding-left: 5px;
        }

        .title-container {
          margin-top: 60px;
          margin-left: 3px;
        }

        .wrap {
          display: flex;
          flex-wrap: wrap;

        }

        .photo {
          display: inline-block;
          margin-bottom: 8px;
          width: calc(50% - 4px);
          margin-right: 0px;
          margin-left: 3px;
          margin-top: 20px;
          text-decoration: none;
          color: black;
        }
 
       .photo:nth-of-type(2n) {
          margin-right: 0;
        }

        @media screen and (min-width: 50em) {
          .photo {
            width: calc(25% - 6px);
          }
          
          .photo:nth-of-type(2n) {
            margin-right: 8px;
          }
          
          .photo:nth-of-type(4n) {
            margin-right: 0;
          }
        }

        figure {
          margin: 0;
          overflow: hidden;
        }

        figcaption {
          margin-top: 15px;
        }

        img {
          border: none;
          max-width: 100%;
          height: auto;
          display: block;
          transition: transform .2s ease-in-out;
        }
        .footer {
          position: absolute;
          bottom: 0;
          width: 100%;
          /* Set the fixed height of the footer here */
          height: 60px;
          line-height: 60px; /* Vertically center the text there */
          background-color: #f5f5f5;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            var movieTitle = $(this).attr('data-title')
            var plot = $(this).attr('data-plot')
            var actors = $(this).attr('data-actor')
            var year = $(this).attr('data-year')
            var final = "<h3>"+movieTitle+"("+year+")</h3><p>"+plot+"</p> <p>Actor : "+actors+"<p>";
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
            
            $("#text-container").empty().append(final);  
        });
        
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body class="no-touch">
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
          <div class="jumbotron jumbotron-fluid">
           <div class="text-media" id="text-container">
           </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <!-- Fixed navbar -->
    <nav class="navbar navbar-fixed-top navbar-dark bg-primary">
      <button class="navbar-toggler hidden-sm-up" type="button" data-toggle="collapse" data-target="#navbarcoll">
       &#9776;
      </button>
      <div class="collapse navbar-toggleable-xs" id="navbarcoll">
          <a class="navbar-brand" href="#">Fresh Tomatoes</a>
        <ul class="nav navbar-nav">
            <li class="nav-item">
            <a class="nav-link" href="#Action">Action <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="#Comedy">Comedy</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="#Drama">Drama</a>
            </li>
        </ul>
      </div>
    </nav>

    <!-- Content For Action -->
    <div class="title-container">
    <h2> Action </h2> <hr>
    </div>
    <div class="wrap" id="Action">
      {movie_tiles_action}
    </div>
    <!-- Content For Comedy -->
    <div class="title-container" id="Comedy">
    <h2> Comedy </h2> <hr>
    </div>
    <div class="wrap">
      {movie_tiles_comedy}
    </div>
    <!-- Content For Drama -->
    <div class="title-container" id="Drama">
    <h2> Drama </h2> <hr>
    </div>
    <div class="wrap">
      {movie_tiles_drama}
    </div>

    <footer class="footer">
      <div class="container">
        <span class="text-muted">Fresh Tomatoes Movie Project</span>
      </div>
    </footer>
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js"><\/script>')</script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="http://getbootstrap.com/assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<a class="photo movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" data-plot="{movie_plot}" data-title="{movie_title}" data-actor="{movie_actor}" data-year="{movie_year}"">
    <figure>

    <img src="{poster_image_url}">
    <figcaption>{movie_title}</figcaption>

    </figure>     
</a>
'''



def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_year = movie.year,
            movie_actor = movie.getActor(movie.starring),
            movie_plot = movie.plot
        )

    return content

def open_movies_page(action,comedy,drama):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles_action=create_movie_tiles_content(action),
        movie_tiles_comedy=create_movie_tiles_content(comedy),
        movie_tiles_drama=create_movie_tiles_content(drama))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)