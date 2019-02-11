# 1. Django Blog
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fkbchojnacki%2Fblog.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fkbchojnacki%2Fblog?ref=badge_shield)



+ [1. Django Blog](#1-django-blog)
+ [2. Opis](#2-opis)
+ [3. Opis ról i uprawnień](#3-opis-ról-i-uprawnień)
+ [4. Opis zastosowanych technologii i rozwiązań](#4-opis-zastosowanych-technologii-i-rozwiązań)
+ [5. Instalacja](#5-instalacja)
    + [5.1. Ubuntu/Debian](#51-ubuntudebian)
        + [5.1.1. Uruchomienie](#511-uruchomienie)
+ [6. Podstawowa Konfiguracja](#6-podstawowa-konfiguracja)
+ [7. Dodawanie Postów](#7-dodawanie-postów)
+ [8. Facebook i Komentarze](#8-facebook-i-komentarze)
+ [9. Statystki odwiedzeń](#9-statystki-odwiedzeń)
+ [10. Newsletter](#10-newsletter)
+ [11. Zmiana danych administratora](#11-zmiana-danych-administratora)
+ [12. Inne funkcjonalności](#12-inne-funkcjonalności)
    + [12.1. Strona o autorze](#121-strona-o-autorze)
    + [12.2. Kontakt](#122-kontakt)
+ [13. Tworzenie kopii zapasowej](#13-tworzenie-kopii-zapasowej)
+ [14. Przeprowadzone testy aplikacji](#14-przeprowadzone-testy-aplikacji)
+ [15. Schemat struktury bazy danych](#15-schemat-struktury-bazy-danych)
    + [15.1. blog_about](#151-blog_about)
    + [15.2. blog_contact](#152-blog_contact)
    + [15.3. blog_email](#153-blog_email)
    + [15.4. blog_facebook](#154-blog_facebook)
    + [15.5. blog_google](#155-blog_google)
    + [15.6. blog_message](#156-blog_message)
    + [15.7. blog_newsletter](#157-blog_newsletter)
    + [15.8. blog_post](#158-blog_post)
    + [15.9. blog_post](#159-blog_post)

# 2. Opis
Użytkownik ma możliwość dodawania postów, tworzenia newslettera oraz integracji z Facebookiem i Twitterem. Ponadto inni mają możliwość dodawania komentarzy pod postami za pośrednictwem Facebooka. Edycja postów odbywa się w sposób WYSIWYG, a autor ma możliwość wstawiania do nich zdjęć, które może wgrać na serwer, oraz m in. filmów z Youtuba. System ma również możliwość korzystania z Google Analytics do analizy osób odwiedzających stronę.

# 3. Opis ról i uprawnień
- anonimowy - może przeglądać posty, dodawać komentarze, wysyłać wiadomości za pomocą formularza kontaktowego, zapisać się lub zrezygnować z newslettera
- administrator - ma on pełnię uprawnień, w celach bezpieczeństwa jest on wylogowywany automatycznie po okresie bezczynności

# 4. Opis zastosowanych technologii i rozwiązań
Rozwiązanie oparto na:
- Django - framework do tworzenia aplikacji internetowych,
- SQLite - baza danych
- CKEditor - edytor WYSIWYG, możliwość wygrywania zdjęć

# 5. Instalacja

## 5.1. Ubuntu/Debian

Do uruchomienia aplikacji potrzebne jest zainstalowany Python w wersji co najmniej 3.6. Można go zainstalować poniższym poleceniem:
 
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3 python3-pip
```

Następnie wymagane jest zainstalowanie zależności aplikacji. Można to wykonać poniższymi poleceniami:

```bash
pip3 install pipenv
pipenv install
pipenv shell
```
Kolejnym krokiem jest przełączenie na skonfigurowanie środowisko wirtualne, stworzeniem bazy danych i wygenerowanie plików statycznych:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

Stwórz teraz konto administratora, który będzie zarządzał blogiem. Upewnij się, że wybrane przez ciebie hasło jest odpowiedniej długości.

```bash
python manage.py createsuperuser 
```

Ustaw również `SECRET_KEY`, znajdujący się na 15 linii w `website/settings.py`. Zalecane jest, aby miał on co najmniej 40 znaków.

Aplikacja jest teraz gotowa do uruchomienia. Można to wykonać poleceniem:

```bash
python manage.py runserver 0.0.0.0:8080
```

Strona powinna się uruchomić i działać pod portem 8080. Jeśli chcesz możesz uruchomić aplikację pod innym portem. Aby zweryfikować jej działanie, wejdź na adres http://127.0.0.1:8080/  za pomocą przeglądarki.


### 5.1.1. Uruchomienie

Aby ponownie uruchomić stronę np. po restarcie komputera wykonaj poniższe polecenia:
```bash
pipenv shell
python manage.py runserver 0.0.0.0:8080
```

# 6. Podstawowa Konfiguracja

Aby zalogować się na konto administratora wejdź na adres `http://localhost:8000/admin/` i zaloguj się za pomocą wcześniej ustanowionego hasła. Przed twoimi oczami ukarze się panel administracyjny.

Wybierz z listy `Ustawienia` i kliknij na nie. Wybierz z listy `Ustawienia`. 

W następnym okienku kliknij również na `Ustawienia`.


Możesz teraz zmienić nazwę bloga lub jego kolorystykę. Kolor możesz wybrać za pomocą np. strony https://www.rapidtables.com/web/color/html-color-codes.html 
Ponadto masz możliwość wyświetlenia, lub ukrycia takich stron jak kontakt, o autorze i newsletter. Aby uruchomić newsletter potrzebnę są zmiany opisane w [dalszej częsci](#Newsletter).

# 7. Dodawanie Postów

Po zalogowaniu masz możliwość dodawania postów. Aby tego dokonać, wróć na stronę główną. I kliknij `Dodaj Post` w pasku nawigacyjnym. 
W nowym okienku wyświetli się edytor. Dodaj tytuł swojego pierwszego posta i wybierz datę kiedy ma się on ukazać. Możesz np. ustawić, że post ma się pojawić jutro, lub mieć wczorajszą datę. Za pomocą następnego pola masz możliwość edycji treści posta. Możesz za pomocą edytora np. dodać do posta zdjęcie lub dołączyć do niego film na Youtubie.
Następnie zaznacz czy dajesz możliwość udostępnienia posta przez Facebooka lub Twitera. Możesz także włączyć komentarze. Włączenie komentarzy oraz Facebooka wymaga dalszej konfiguracji. Zapisz stronę.
Zostaniesz przekierowany na nowoutworząną stronę. Jeśli jesteś zalogowany, masz możlowość edycji postu, klikając na  ikonę notesu. Zaawansowana edycja oraz usunięcie strony można wykonać za pomocą panelu administracyjnego.


# 8. Facebook i Komentarze
Aby umożliwić dodawanie komentarzy, jak i zintegrować aplikację z Facebookiem, zarejestruj ją na stronie `https://developers.facebook.com/` Następnie dodaj uzyskany numer aplikacji do panelu administracyjnego klikając dodaj przy `Facebook identyfikator aplikacji`. Po zapisaniu zmian aplikacja powinna być już zintegrowana z serwisem.

# 9. Statystki odwiedzeń
Do wyświetlania zaawansowanych statystyk niezbędne jest utworzenie konta w Google Analytics. Możesz to zrobić rejestrując stronę na pod adresem `https://analytics.google.com/analytics/web/`. Wklej otrzymany identyfikator śledenia do panelu administracyjnego klikając dodaj przy `Google Analitycs identyfikator śledzenia` . Po zapisaniu zmian na stronie `https://analytics.google.com/analytics/web/` będziesz widział statystyki dotyczące twojego serwisu.

# 10. Newsletter
Aby odblokować wejdź jako administrator w ustawienia i zaznacz, aby strona newslettera była widoczna. Sposób wejścia w ustawienia jest opisany w sekcji [6. Podstawowa Konfiguracja](#6-podstawowa-konfiguracja). Zapisz zmiany i wróć do widoku głównego panelu administracyjnego. Kliknij dodaj przy `Konfiguracja serwera email`. Uzupełnij wymagane dane. Dane jakimi należy uzupełnić formularz są dostępne u dostawców pocztowych. Np. dla Gmaila konfiguracja jest następująca:
```
Serwer SMTP: smtp.gmail.com
Port SSL: 465
Użytkownik: uzytkownik@gmail.com
Hasło: hasłoUżytkownika
```
Powyższa konfiguracja, jak i więcej informacji dotyczące Gmaila jest dostępne pod https://support.google.com/mail/answer/7126229 
Po zapisaniu zmian i wróceniu na stronę główną pojawi ci się nowa opcja w panelu nawigacyjnym `Wyślij newsletter`. Uzupełnij temat i treść wiadomości. Po kliknięciu `wyślij`, wiadomość zostanie przesłana na skrzynki pocztowe osób zapisanych do newslettera. Jeśli się wylogujesz zobaczysz nową opcję Newsletter. Kliknij na nią, uzupełnij pole `Email`, a następnie wybierz przycisk dodaj. Jeśli poprawnie skonfigurowałeś pocztę powinieneś dostać na wyznaczoną skrzynkę link aktywacyjny. Po jego kliknięciu twoje email zostanie dodany na listę Newslettera. Każdy zapisany i aktywowany użytkownik w otrzymanych wiadomościach otrzymuje informację, w jak w sposób automatyczny wypisać się z listy. Zapisanych użytkowników możesz zobaczyć w panelu administracyjnym w sekcji `Zapisani do newslettera`.

# 11. Zmiana danych administratora
Możesz utworzyć kilka kont administratora poleceniem:

```bash
python manage.py createsuperuser 
```
Ponadto w panelu administracyjnym w sekcji `Użytkownicy`, masz możliwość edycji danych użytkownika.

# 12. Inne funkcjonalności

## 12.1. Strona o autorze
Korzystając z informacji zawartych w [6. Podstawowa Konfiguracja](#6-podstawowa-konfiguracja) odblokuj stronę o autorze. Wróć na stronę główną aplikacji. Zobaczysz w pasku nową stronę `Edytuj o autorze`. Po jej wybraniu zamieść w edytorze kilka słów o sobie i zapisz zmiany. Zostaniesz teraz przekierowany na stronę `O autorze` z twoimi informacjami.

## 12.2. Kontakt
Odblokuj stronę kontaktów na stronie ustawień, jak wejść w ustawienie jest zawarte w sekcji [6. Podstawowa Konfiguracja](#6-podstawowa-konfiguracja). Wejdź na stronę główną aplikacji. Po prawej stronie będziesz miał informację o ilości nieprzeczytanych wiadomości ze strony kontaktowej. Po kliknięciu na przycisk informujący o wiadomościach zostaniesz przeniesiony do panelu administracyjnego. Masz dostęp do wszystkich wiadomości. Po kliknięciu na wiadomość masz możliwość jej przeczytania. Możesz również zaznaczyć, że ją przeczytałeś.
Wyloguj się, na stronie głównej zobaczysz nową stronę o nazwie `Kontakt`. Aby wysłać wiadomość do administratora, uzupełnij pola wymaganymi informacjami. Po kliknięciu wyślij, gdy ponownie się zalogujesz, dostaniesz informację o nowej wiadomości.

# 13. Tworzenie kopii zapasowej

Wszystkie zapisane informację są przechowywane w pliku `db.sqlite3`, w głównym folderze aplikacji. Aby wykonać kopię zapasową, wystarczy wyłączyć aplikację i skopiować wspomniany plik.

# 15. Przeprowadzone testy aplikacji
Aplikacja została przetestowana i uruchomiona na zewnętrznym serwerze testowym. Konfiguracja ta obejmowała Dockera, i Nginxa służącego jako Reverse proxy.

# 15. Schemat struktury bazy danych

Pomiędzy zaprojektowanymi encjami używanymi w tym systemie nie występują żadne związki.


## 15.1. blog_about
Dotyczy strony o autorze
```
id - integer - id
about - varchar - treść strony o autorze
```

## 15.2. blog_contact
Dotyczy strony kontakt
```
id - integer - id
name - varchar - imię i nazwisko osoby korzystającej z kontaktu
email - varchar - email korzystającej z kontaktu
text - text - zawartość wiadomości
read - bool - czy przeczytano przez administratora
```

## 15.3. blog_email
Dotyczy konfiguracji emaila
```
id - integer - id
smtp - varchar - adres serwera SMTP
sslPort - varchar - port serwera SMTP
password - varchar -  hasło do serwera SMTP
email - varchar - login so serwera SMTP
```


## 15.4. blog_facebook
Konfiguracja facebooka
```
id - integer - id
appId - varchar - identyfikator Facebooka
```

## 15.5. blog_google
Konfiguracja Google Analytics
```
id - integer - id
appId - varchar - identyfikator Google Analytics
```

## 15.6. blog_message
Wiadomość wysłana za pomocą newslettera
```
id - integer - id
title - varchar - tytuł wiadomości
creeated_date - date - data wysłania
text - text - treść wiadomości
```

## 15.7. blog_newsletter
Przechowuje dane dotyczące osoby zapisanej do newslettera
Wiadomość wysłana za pomocą newslettera
```
id - integer - id
email - varchar - email
confirmed - bool - czy konto jest potwierdzone poprzez kliknięcie w link aktywacyjny
code - varchar - kod aktywacyjny, kod na usunięcie z listy
created_date - date - data zapisania
```

## 15.8. blog_post
Przechowuje post
```
id - integer - id
title - varchar - tytuł postu
text - text - treść postu
created_date - date - data utworzenia
published_date - date - data opublikowania
author_id - integer - identyfikator autora
facebook - bool - czy jest aktywny przycisk udostępnienia, polubienia przez Facebooka
twitter - bool - czy jest aktywny przycisk udostępnienia przez Twittera
comments - bool - czy komentarze są aktywne
```

## 15.9. blog_post
Przechowuje konfigurację bloga
```
id - integer - id
title - varchar - tytuł bloga
post_color - varchar - kolor tytułów postów zapisany w formie szesnastkowej
navbar_color - varchar - kolor paska nawigacyjnego zapisany w formie szesnastkowej
navbar_text_color - varchar - kolor tekstu paska nawigacyjnego zapisany w formie szesnastkowej
about_enabled - bool - czy strona 'o autorze' jest aktywna
contact_enabled - bool - czy strona 'kontakt' jest aktywna
newsletter_enabled - bool - czy strona 'newsletter' jest aktywna
custom_css - text - własny styl css
```




## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fkbchojnacki%2Fblog.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fkbchojnacki%2Fblog?ref=badge_large)