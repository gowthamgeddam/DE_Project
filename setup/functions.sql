-- 1. Get movie_id, release_year, imdb_rating by movie_name 
CREATE OR REPLACE FUNCTION get_movie_details(movie_name VARCHAR) 
RETURNS TABLE ( 
    movie_id BIGINT, 
    release_year INT, 
    imdb_rating DOUBLE PRECISION 
) AS $$ 
BEGIN 
    RETURN QUERY 
    SELECT 
        m.id AS movie_id, 
        rd.release_year, 
        id.vote_average AS imdb_rating 
    FROM 
        movie m 
    JOIN 
        release_details rd ON m.id = rd.id 
    JOIN 
        imdb_details id ON m.id = id.id 
    WHERE 
        m.original_title = movie_name 
    LIMIT 1; 
END; 
$$ LANGUAGE plpgsql; 
 
-- 2. Get actor’s Highest grossing movie 
CREATE OR REPLACE FUNCTION get_actor_highest_grossing_movie(p_actor_name VARCHAR) 
RETURNS VARCHAR AS $$ 
DECLARE 
highest_grossing_movie VARCHAR; 
BEGIN 
SELECT m.original_title INTO highest_grossing_movie 
FROM movie_cast mc 
JOIN movie m ON mc.id = m.id 
JOIN finances f ON m.id = f.id 
WHERE mc.actor_name = p_actor_name 
ORDER BY f.revenue DESC 
LIMIT 1; 
RETURN highest_grossing_movie; 
END; 
$$ LANGUAGE plpgsql;

-- 3. Get director of a movie 
CREATE OR REPLACE FUNCTION get_movie_director(movie_title VARCHAR) 
RETURNS VARCHAR AS $$ 
DECLARE 
director_name VARCHAR; 
BEGIN 
SELECT dr.director_name INTO director_name 
FROM movie m 
JOIN directed dr ON m.id = dr.id 
WHERE m.original_title = movie_title 
LIMIT 1; 
RETURN director_name; 
END; 
$$ LANGUAGE plpgsql; 

-- 4. Count movie number by year 
CREATE OR REPLACE FUNCTION count_movies_by_year(p_year INT) 
RETURNS INT AS $$ 
DECLARE 
movie_count INT; 
BEGIN 
SELECT COUNT(*) INTO movie_count 
FROM release_details 
WHERE release_year = p_year; 
RETURN movie_count; 
END; 
$$ LANGUAGE plpgsql; 

-- 5. Get genre name by movie name 
CREATE OR REPLACE FUNCTION get_genre_by_movie(movie_title VARCHAR) 
RETURNS TABLE(genre_name VARCHAR) AS $$ 
BEGIN 
RETURN QUERY 
SELECT mg.genre 
FROM movie m 
JOIN movie_genre mg ON m.id = mg.id 
WHERE m.original_title = movie_title; 
END; 
$$ LANGUAGE plpgsql; 

-- TRIGGERS --

-- 1.  Create a logging table to store information about new movies added 
-- CREATE TABLE movie_log ( 
-- log_id SERIAL PRIMARY KEY, 
-- movie_id INT, 
-- title VARCHAR(255), 
-- release_year INT, 
-- added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
-- );
-- -- Create the trigger function to log new movie entries 
-- CREATE OR REPLACE FUNCTION log_new_movie() 
-- RETURNS TRIGGER AS $$ 
-- BEGIN -- Insert information about the new movie into the log table 
-- INSERT INTO movie_log (movie_id, title, release_year) 
-- VALUES (NEW.id, NEW.original_title, NEW.release_year); 
-- RETURN NEW; 
-- END; 
-- $$ LANGUAGE plpgsql;

-- -- Create the trigger to call the log function after a new movie is inserted 
-- CREATE TRIGGER log_new_movie 
-- AFTER INSERT ON movie 
-- FOR EACH ROW 
-- EXECUTE FUNCTION log_new_movie(); -- Create a logging table to store information about deleted movies 
-- CREATE TABLE movie_deletion_log ( 
-- log_id SERIAL PRIMARY KEY, 
-- movie_id INT, 
-- title VARCHAR(255), 
-- deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
-- ); 

-- -- 2. Create the trigger function to log movie deletions 
-- CREATE OR REPLACE FUNCTION log_movie_deletion() 
-- RETURNS TRIGGER AS $$ 
-- BEGIN -- Insert information about the deleted movie into the log table 
-- INSERT INTO movie_deletion_log (movie_id, title, deleted_at) 
-- VALUES (OLD.id, OLD.original_title, CURRENT_TIMESTAMP); 
-- RETURN OLD; 
-- END; 
-- $$ LANGUAGE plpgsql;

-- -- Create the trigger to call the log function after a movie is deleted 
-- CREATE TRIGGER log_movie_deletion 
-- AFTER DELETE ON movie 
-- FOR EACH ROW 
-- EXECUTE FUNCTION log_movie_deletion(); 