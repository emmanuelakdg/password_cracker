<!DOCTYPE html>
<html>
    <head>
        <title>Formulaire d'authentification</title>
        <link rel="stylesheet" href="login.css">
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
              <form>
                <input type="text" id="login" class="fadeIn second" name="login" placeholder="login" required>
                <input type="password" id="password" class="fadeIn third" name="password" placeholder="password">
                <input type="submit" class="fadeIn fourth" value="Log In">
              </form>
          
              <!-- Remind Passowrd -->
              <div id="formFooter">
                <a class="underlineHover" href="#">Forgot Password?</a>
              </div>
          
            </div>
          </div>

          <?php
  
  
          if (isset($_POST['login'], $_POST['password'] )){
            $login = $_POST['login'];
            $password = $_POST['password'];
            if ($login === 'admin' && $password === 'passe') {
              echo 'Authentification réussie !';
            } else {
              echo 'Identifiants invalides. Veuillez réessayer.';
          }
          }
          
          ?>
          
    </body>
</html>