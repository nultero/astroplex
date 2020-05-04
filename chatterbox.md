---
permalink: /projects/chatterbox
---

<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1 shrink-to-fit=no">
    <title>holoplex</title>

    <!-- favicon -->
    <link rel="apple-touch-icon" sizes="60x60" href="/static/images/favicons/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/static/images/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/static/images/favicons/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="mask-icon" href="/static/images/favicons/safari-pinned-tab.svg" color="#5bbad5">
    <meta name="msapplication-TileColor" content="#da532c">
    <meta name="theme-color" content="#ffffff">



    <!-- boot -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <!-- font index -->
    <link href="https://fonts.googleapis.com/css?family=Quicksand&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Righteous&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Kelly+Slab&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Orbitron&display=swap" rel="stylesheet">    


    <!-- my custom css -->
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
  </head>

  <body onload="loadFunction()">


    <div id="meteor-medium"></div>
    <div id="meteor-midtext"></div>
    <div id="meteor-outermost"></div>
    <div id="meteor-fast"></div>


<!-- this is the content — div that responds to the pop -->

<div class="container animatebottom popUpText" id="pageShowAfterLoad"> 
        <h2 class="center-align astroText">
        <nav class="navbar" aria-label="breadcrumb">
          <ol class="navbar breadcrumb">
           <li class="navbar breadcrumb-item"><a href=".." id="astroTextNoPadNavHeader">Λ</a></li>
           <li class="navbar breadcrumb-item"><a href=".">holoplex</a></li>
           <li class="navbar breadcrumb-item active" id="astroTextNoPadNav" aria-current="page">^ chatterbox</li>
          </ol>
          </nav>
          </h2>
      
    

      <hr id="topPageRule">

      <h4 class="center-align astroText">This post has yet to be written. Check back later for more information.</h4>

      
</div>



    <script>
      var myLoadThingy;
      
      function loadFunction() {
        myLoadThingy = setTimeout(showPage, 1300);
      }
      
      function showPage() {
        document.getElementById("meteor-medium").style.display = "none";
        document.getElementById("meteor-midtext").style.display = "none";
        document.getElementById("meteor-outermost").style.display = "none";
        document.getElementById("meteor-fast").style.display = "none";
        document.getElementById("pageShowAfterLoad").style.display = "block";
      }
      </script>
  </body>
</html>