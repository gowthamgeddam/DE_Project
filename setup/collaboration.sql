create table collaboration as
(WITH DirectorActorCollab AS (
    SELECT 
        d.director_name,
        c.actor_name,
        COUNT(m.id) AS collab_count,
        MAX(f.revenue) AS highest_revenue
    FROM 
        directed d
    JOIN 
        movie m ON d.id = m.id
    JOIN 
        movie_cast c ON m.id = c.id
    JOIN 
        finances f ON m.id = f.id
    GROUP BY 
        d.director_name, c.actor_name
),
TopCollab AS (
    SELECT 
        director_name,
        actor_name,
        collab_count,
        highest_revenue,
        ROW_NUMBER() OVER (PARTITION BY director_name ORDER BY collab_count DESC) AS rn
    FROM 
        DirectorActorCollab
)
SELECT 
    tc.director_name,
    tc.actor_name,
    tc.collab_count,
    m.original_title AS highest_grossing_movie
FROM 
    TopCollab tc
JOIN 
    movie m ON m.id = (
        SELECT m2.id
        FROM movie m2
        JOIN finances f2 ON m2.id = f2.id
        JOIN movie_cast c2 ON m2.id = c2.id
        WHERE 
            tc.actor_name = c2.actor_name AND 
            f2.revenue = tc.highest_revenue
        LIMIT 1
    )
WHERE 
    tc.rn = 1
ORDER BY 
    tc.collab_count DESC
)
	
