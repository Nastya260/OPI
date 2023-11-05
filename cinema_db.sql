create database cinema_opi
use cinema_opi
-- Таблиця фільмів
CREATE TABLE Movies (
  id INT NOT NULL IDENTITY(1,1),
  name VARCHAR(255) NOT NULL,
  genre VARCHAR(255) NOT NULL,
  duration INT NOT NULL,
  description VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

-- Таблиця сеансів
CREATE TABLE Sessions (
  id INT NOT NULL IDENTITY(1,1),
  id_movie INT NOT NULL,
  id_hall INT NOT NULL,
  date DATE NOT NULL,
  time TIME NOT NULL,
  price INT NOT NULL,
  PRIMARY KEY (id)
);

-- Таблиця місць
CREATE TABLE Seats (
  id INT NOT NULL IDENTITY(1,1),
  row INT NOT NULL,
  seat INT NOT NULL,
  PRIMARY KEY (id)
);

-- Таблиця квитків
CREATE TABLE Tickets (
  id INT NOT NULL IDENTITY(1,1),
  number INT NOT NULL,
  id_user INT NOT NULL,
  id_session INT NOT NULL,
  id_seat INT NOT NULL,
  PRIMARY KEY (id)
);

-- Таблиця користувачів
CREATE TABLE Users (
  id INT NOT NULL IDENTITY(1,1),
  number DECIMAL NOT NULL,
  email VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
-- Заповнення таблиці фільмів
INSERT INTO Movies (name, genre, duration, description)
VALUES
('Володар перснів: Повернення короля', 'Фентезі', 240, 'Епічний фільм про війну добра зі злом'),
('Хрещений батько', 'Кримінальний бойовик', 190, 'Історія про мафіозну сім`ю Корлеоне'),
('12 розгніваних чоловіків', 'Драма', 200, 'Історія про 12 присяжних, які повинні винести вердикт у справі про вбивство'),
('Початок', 'Наукова фантастика', 148, 'Історія про людину, яка може проникати в сни'),
('Титанік', 'Романтична драма', 194, 'Історія кохання між бідним художником і багатою спадкоємицею');

-- Заповнення таблиці сеансів
INSERT INTO Sessions (id_movie, id_hall, date, time, price)
VALUES
(1, 1, '2023-11-06', '19:00', 200),
(2, 2, '2023-11-07', '21:00', 300),
(3, 3, '2023-11-08', '18:00', 150),
(4, 4, '2023-11-09', '20:00', 100),
(5, 5, '2023-11-10', '17:00', 50);

-- Заповнення таблиці місць
INSERT INTO Seats (row, seat)
VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 2),
(2, 3),
(3, 1),
(3, 2),
(3, 3);

-- Заповнення таблиці квитків
INSERT INTO Tickets (number, id_user, id_session, id_seat)
VALUES
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 3),
(4, 4, 4, 4),
(5, 5, 5, 5);