-- user_0d_1 istifadəçisini yaratmaq üçün SQL skript
-- Bu skript MySQL serverdə root istifadəçisi kimi işlədilməlidir

-- İstifadəçini yaradırıq (əgər artıq mövcud deyilsə)
-- IF NOT EXISTS istifadə edirik ki, əgər istifadəçi artıq varsa xəta verməsin
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- İstifadəçiyə bütün icazələri veririk
-- *.* bütün bazalarda və bütün cədvəllərdə deməkdir
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- İcazə dəyişikliklərini tətbiq edirik
FLUSH PRIVILEGES;
