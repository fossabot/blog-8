from .models import Post, Facebook, Google


def getGoogleScript():
    googles = Google.objects.values_list('appId', flat=True)
    google = str(googles[0] ) if len(googles)>0 else None
    googleScript = """
        <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={@googleId}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '{@googleId}');
</script>
    """.replace("{@googleId}","" if google is None else google)
    return googleScript if google != "" else None

def getFacebookScript(facebook):
    facebookScript = """
        <div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = 'https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.2&appId={@facebookId}&autoLogAppEvents=1';
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
    """.replace("{@facebookId}","" if facebook is None else facebook)
    return facebookScript