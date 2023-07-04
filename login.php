<!DOCTYPE html>
<html>
    <head>
        <title>Formulaire d'authentification</title>
        <link rel="stylesheet" href="login.css">
        <meta charset="UTF-8">
    </head>
    <body>
        <div class="wrapper fadeInDown">
            <div id="formContent">
              <!-- Tabs Titles -->
              <h2 class="active"> Sign In </h2>          
              <!-- Icon -->
              <div class="fadeIn first">
                <img src="user-286.png" id="icon" alt="User Icon" />
              </div>
          
              <!-- Login Form -->
              <form method="POST" action="login.php">
                <input type="text" id="login" class="fadeIn second" name="login" placeholder="login" required>
                <input type="password" id="password" class="fadeIn third" name="password" placeholder="password">
                <input type="submit" class="fadeIn fourth" value="Log In">
              </form>
          
              <!-- Remind Passowrd -->
              <div id="formFooter">
                <a class="underlineHover" href="#">Forgot Password?</a>


                <p>
                  <?php
                      if (isset($_POST['login'], $_POST['password'] )) {
                        $login = $_POST['login'];
                        $password = $_POST['password'];
                        if ($login === 'admin' && $password === 'pluie') {
                          echo 'Authentification reussie !';
                        } else {
                          echo 'Identifiants invalides. Veuillez réessayer.';
                        }
                    }
                  ?>
                </p>


                
              </div>
          
            </div>
          </div>

          
          
    </body>
</html>