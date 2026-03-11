CREATE DATABASE digital_clock_db;

USE digital_clock_db;

CREATE TABLE settings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    theme VARCHAR(30),
    time_format VARCHAR(10),
    city VARCHAR(50)
);

-- Insert some sample data
INSERT INTO settings (username, theme, time_format, city)
VALUES
('Rahul', 'darkly', '24hr', 'New Delhi'),
('Ananya', 'cosmo', '12hr', 'Mumbai'),
('Karan', 'flatly', '24hr', 'Bangalore');
