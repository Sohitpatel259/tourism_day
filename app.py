import qrcode
import os
import pathlib

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Famous Personalities of Mexico</title>
    <style>
        /* CSS Variables for theming */
        :root {
            --bg-color-light: #f4f4f9;
            --text-color-light: #333;
            --header-bg-light: #ffffff;
            --accent-color-light: #007bff;
            --accordion-bg-light: #ffffff;
            --accordion-hover-light: #e9e9ed;
            --border-color-light: #ddd;
            --correct-light: #28a745;
            --incorrect-light: #dc3545;

            --bg-color-dark: #121212;
            --text-color-dark: #e0e0e0;
            --header-bg-dark: #1e1e1e;
            --accent-color-dark: #4dabf7;
            --accordion-bg-dark: #2c2c2c;
            --accordion-hover-dark: #3a3a3a;
            --border-color-dark: #444;
            --correct-dark: #77dd77;
            --incorrect-dark: #ff6961;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 20px;
            transition: background-color 0.3s, color 0.3s;
        }

        /* Light Theme (Default) */
        body.theme-light {
            background-color: var(--bg-color-light);
            color: var(--text-color-light);
        }
        body.theme-light .container {
            background-color: var(--header-bg-light);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        body.theme-light .accordion {
            background-color: var(--accordion-bg-light);
            border: 1px solid var(--border-color-light);
        }
        body.theme-light .accordion:hover {
            background-color: var(--accordion-hover-light);
        }
        body.theme-light .theme-btn.active {
            background-color: var(--accent-color-light);
            color: white;
        }
        body.theme-light .category-title {
            border-bottom: 2px solid var(--accent-color-light);
        }
        body.theme-light .quiz-check-btn {
            background-color: var(--accent-color-light);
            color: white;
        }
        body.theme-light .quiz-feedback.correct, body.theme-light .correct-answer { color: var(--correct-light); }
        body.theme-light .quiz-feedback.incorrect { color: var(--incorrect-light); }


        /* Dark Theme */
        body.theme-dark {
            background-color: var(--bg-color-dark);
            color: var(--text-color-dark);
        }
        body.theme-dark .container {
            background-color: var(--header-bg-dark);
            box-shadow: 0 4px 8px rgba(0,0,0,0.4);
        }
        body.theme-dark .accordion {
            background-color: var(--accordion-bg-dark);
            border: 1px solid var(--border-color-dark);
        }
        body.theme-dark .accordion:hover {
            background-color: var(--accordion-hover-dark);
        }
        body.theme-dark .theme-btn.active {
            background-color: var(--accent-color-dark);
            color: var(--bg-color-dark);
        }
        body.theme-dark .category-title {
            border-bottom: 2px solid var(--accent-color-dark);
        }
        body.theme-dark .quiz-check-btn {
            background-color: var(--accent-color-dark);
            color: var(--bg-color-dark);
        }
        body.theme-dark .quiz-feedback.correct, body.theme-dark .correct-answer { color: var(--correct-dark); }
        body.theme-dark .quiz-feedback.incorrect { color: var(--incorrect-dark); }


        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 25px;
            border-radius: 10px;
        }

        h1, #score-board {
            text-align: center;
        }
        #score-board {
            margin: -10px 0 25px 0;
            font-size: 1.5em;
            font-weight: bold;
        }
        
        .theme-selector {
            text-align: center;
            margin-bottom: 30px;
        }

        .theme-btn {
            padding: 10px 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background: none;
            color: inherit;
            font-size: 16px;
            cursor: pointer;
            margin: 0 5px;
            transition: background-color 0.3s, color 0.3s;
        }

        .category-title {
            font-size: 2em;
            margin-top: 40px;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        .accordion {
            cursor: pointer;
            padding: 18px;
            width: 100%;
            text-align: left;
            border-radius: 5px;
            margin-bottom: 5px;
            transition: background-color 0.3s;
            font-size: 18px;
            font-weight: bold;
        }

        .accordion.active, .accordion:hover { }
        
        .panel {
            padding: 0 18px;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out;
            line-height: 1.6;
        }

        .panel p { margin-top: 15px; }
        .panel h4 { margin-top: 20px; margin-bottom: 5px; }

        /* --- QUIZ STYLES --- */
        .quiz-container {
            margin-top: 25px;
            padding-top: 20px;
            border-top: 1px dashed #ccc;
        }
        .quiz-question {
            font-weight: bold;
            margin-bottom: 10px;
        }
        .quiz-options label {
            display: block;
            margin-bottom: 8px;
            cursor: pointer;
        }
        .quiz-check-btn {
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            font-size: 14px;
            cursor: pointer;
            margin-top: 10px;
        }
        .quiz-check-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }
        .quiz-feedback {
            margin-top: 10px;
            font-weight: bold;
            min-height: 20px;
        }
        .correct-answer {
            font-weight: bold;
        }

    </style>
</head>
<body class="theme-light">

    <div class="container">
        <h1>Famous Personalities of Mexico</h1>
        
        <h2 id="score-board">Score: <span id="score-value">0</span> / 15</h2>

        <div class="theme-selector">
            <span>Select Theme:</span>
            <button class="theme-btn active" data-theme="theme-light">Light ☀️</button>
            <button class="theme-btn" data-theme="theme-dark">Dark 🌙</button>
        </div>

        <div class="content">
            <h2 class="category-title">Arts and Literature 🎨</h2>
            <div class="accordion">1. Frida Kahlo (1907-1954)</div>
            <div class="panel">
                <h4>Early Life and Defining Accident</h4>
                <p>Born Magdalena Carmen Frieda Kahlo y Calderón in Coyoacán, Mexico City, Frida Kahlo's life was shaped by both physical and emotional turmoil. At age six, she contracted polio, which left her right leg thinner than her left, a source of insecurity she would later conceal with her iconic long skirts. A far more devastating event occurred in 1925 when a tram collided with the bus she was riding. She suffered near-fatal injuries, including a broken spinal column, collarbone, ribs, pelvis, and multiple fractures in her right leg and foot. An iron handrail impaled her through her abdomen. During her agonizingly slow recovery, confined to a full-body cast, Kahlo began to paint. Her father, a photographer, gave her a specially made easel, and a mirror was placed above her bed, allowing her to become her own primary subject. This introspection born from suffering became the cornerstone of her artistic canon.</p>
                <h4>Artistic Career and Themes</h4>
                <p>Kahlo's work is a raw and vibrant exploration of her personal reality. Unlike many of her contemporaries who were focused on grand public murals, her canvases were intimate and often shocking. She produced around 200 paintings, 55 of which are self-portraits. These works are filled with symbolism, blending realism with fantasy to explore themes of identity, pain, the human body, and death. She depicted her physical suffering from the accident, her turbulent marriage to Diego Rivera, her miscarriages, and her deep connection to her Mexican heritage. She incorporated elements of Mexican folk art, pre-Columbian artifacts, and Catholic iconography into a style that André Breton once labeled as Surrealist, a tag Kahlo herself rejected, stating, "I never painted dreams. I painted my own reality."</p>
                <h4>Legacy and Impact</h4>
                <p>During her lifetime, Kahlo was more known as Diego Rivera's wife than as an artist in her own right. It was not until decades after her death that her work received widespread international acclaim. Today, she is a global icon, celebrated not only for her groundbreaking art but also as a symbol of feminism, resilience, and countercultural defiance. Her unibrow, her bold fashion sense incorporating traditional Tehuana dresses, and her unapologetic depiction of the female experience have cemented her status as one of the most influential artists of the 20th century.</p>
                <div class="quiz-container" data-correct="b">
                    <p class="quiz-question">What pivotal event led Frida Kahlo to begin painting?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-frida" value="a"> Contracting polio as a child</label>
                        <label><input type="radio" name="quiz-frida" value="b"> A near-fatal bus accident</label>
                        <label><input type="radio" name="quiz-frida" value="c"> Her marriage to Diego Rivera</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>

            <div class="accordion">2. Diego Rivera (1886-1957)</div>
            <div class="panel">
                <h4>Early Life and European Influence</h4>
                <p>Born in Guanajuato, Diego Rivera showed artistic talent from a young age. He began studying at the Academy of San Carlos in Mexico City at just ten years old. In 1907, with the support of a patron, he traveled to Europe, where he would spend the next 14 years. In Spain, he studied the works of masters like Goya and El Greco, and in Paris, he immersed himself in the avant-garde movements, becoming a prominent figure in the Cubist circle alongside Pablo Picasso. This period was crucial for developing his technique and understanding of modern art.</p>
                <h4>Return to Mexico and Muralism</h4>
                <p>Upon his return to Mexico in 1921, Rivera was a changed man. The Mexican Revolution had reshaped the nation's political and cultural landscape. Encouraged by the new government's Secretary of Public Education, José Vasconcelos, Rivera, along with David Alfaro Siqueiros and José Clemente Orozco, began to create a new form of public art: muralism. His goal was to create art that was accessible to all people, not just the elite, and that could educate the largely illiterate population about Mexico's history, struggles, and aspirations. His most famous murals, such as those in the National Palace in Mexico City and the Secretariat of Public Education, are epic narratives that glorify Mexico's indigenous heritage, celebrate its revolutionary heroes, and critique capitalism and the ruling class from a Marxist perspective.</p>
                <h4>Personal Life and Legacy</h4>
                <p>Rivera's personal life was as dramatic as his art. He was married four times, most famously twice to Frida Kahlo. Their relationship was a tempestuous union of two powerful artistic forces, marked by mutual passion, infidelity, and deep intellectual connection. Despite his controversial communist politics, which led to the infamous destruction of his "Man at the Crossroads" mural at Rockefeller Center in New York, Rivera's influence is undeniable. He is credited with helping to shape a post-revolutionary Mexican identity and is celebrated as one of the most important artists of the 20th century.</p>
                <div class="quiz-container" data-correct="c">
                    <p class="quiz-question">Upon returning to Mexico, Diego Rivera became a leading figure in which art movement?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-rivera" value="a"> Cubism</label>
                        <label><input type="radio" name="quiz-rivera" value="b"> Surrealism</label>
                        <label><input type="radio" name="quiz-rivera" value="c"> Muralism</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>
            
            <div class="accordion">3. Octavio Paz (1914-1998)</div>
            <div class="panel">
                <h4>Early Life and Literary Beginnings</h4>
                <p>Octavio Paz was born in Mexico City during the Mexican Revolution, a conflict that deeply influenced his family and his worldview. His grandfather was a liberal novelist and intellectual with a vast library where Paz first encountered literature. He published his first collection of poetry, Luna Silvestre (Wild Moon), at the age of 19. His early work was influenced by Marxism and Surrealism. A pivotal experience was his participation in the Second International Writers' Congress in Spain in 1937 during the Spanish Civil War, which solidified his anti-fascist convictions but also began his disillusionment with the rigidity of Stalinism.</p>
                <h4>Major Works and Diplomatic Career</h4>
                <p>Paz's career was a dual track of literary production and diplomatic service. He joined the Mexican diplomatic service in 1945 and served in various posts, including as ambassador to India from 1962 to 1968. His time in India profoundly influenced his poetry and thought, introducing him to Eastern philosophy and spirituality. His most famous work is the book-length essay El laberinto de la soledad (The Labyrinth of Solitude, 1950), a profound analysis of the Mexican national character, exploring its history, myths, and psychology. His poetry, collected in volumes like Piedra de sol (Sunstone) and Blanco, is known for its lyrical intensity and intellectual rigor. He resigned from his ambassadorship in 1968 in protest of the Mexican government's Tlatelolco massacre of student demonstrators.</p>
                <h4>Nobel Prize and Legacy</h4>
                <p>In 1990, Octavio Paz was awarded the Nobel Prize in Literature for "impassioned writing with wide horizons, characterized by sensuous intelligence and humanistic integrity." The Nobel committee recognized his ability to bridge poetry and prose, and to explore the intersections of love, politics, and identity. He remains a towering figure in world literature, a poet-philosopher who sought to understand the essence of his nation and the shared solitude of humanity.</p>
                <div class="quiz-container" data-correct="a">
                    <p class="quiz-question">Which book-length essay by Octavio Paz is a famous analysis of the Mexican national character?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-paz" value="a"> The Labyrinth of Solitude</label>
                        <label><input type="radio" name="quiz-paz" value="b"> Sunstone</label>
                        <label><input type="radio" name="quiz-paz" value="c"> Wild Moon</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>
            
            <div class="accordion">4. Juan Rulfo (1917-1986)</div>
            <div class="panel">
                <h4>A Life Shaped by Violence</h4>
                <p>Juan Rulfo's childhood in rural Jalisco was scarred by the violence of the Cristero War, a brutal conflict between the government and Catholic rebels. His father was assassinated in 1923, and his mother died of a heart attack in 1927. Orphaned at a young age, he was sent to an orphanage in Guadalajara. This early exposure to death, desolation, and the harsh realities of rural Mexican life would become the bedrock of his literary universe. He moved to Mexico City in the mid-1930s and worked various jobs, including as an immigration agent and later in sales for a tire company, which allowed him to travel extensively through the Mexican countryside that so defined his writing.</p>
                <h4>A Slim but Monumental Body of Work</h4>
                <p>Rulfo's literary output is famously sparse but profoundly influential. He published only two books: the short story collection El llano en llamas (The Burning Plain, 1953) and the novel Pedro Páramo (1955). The Burning Plain is a collection of stark, realistic stories depicting the poverty, violence, and fatalism of life in rural Mexico. Pedro Páramo is his masterpiece, a revolutionary novel that tells the story of a man who travels to his late mother's hometown of Comala in search of his father, only to find a literal ghost town populated by whispering spirits. The novel's fragmented structure, its blend of the real and the supernatural, and its haunting atmosphere made it a foundational text of magical realism.</p>
                <h4>Legacy as a "Writer's Writer"</h4>
                <p>After the publication of Pedro Páramo, Rulfo largely abandoned creative writing, dedicating himself to photography and working for the National Institute for Indigenous Peoples. Despite his small output, his influence is immense. Writers like Gabriel García Márquez have cited Rulfo as a major inspiration, with García Márquez claiming he could recite Pedro Páramo from memory and that it changed his life. Rulfo's work perfectly captures the silence, mystery, and sorrow of the Mexican landscape and its people, making him one of the most esteemed writers in the Spanish language.</p>
                <div class="quiz-container" data-correct="b">
                    <p class="quiz-question">Which novel by Juan Rulfo is considered a masterpiece of magical realism?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-rulfo" value="a"> The Burning Plain</label>
                        <label><input type="radio" name="quiz-rulfo" value="b"> Pedro Páramo</label>
                        <label><input type="radio" name="quiz-rulfo" value="c"> The Golden Cockerel</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>

            <div class="accordion">5. Rufino Tamayo (1899-1991)</div>
            <div class="panel">
                <h4>Forging an Independent Path</h4>
                <p>Rufino Tamayo was born in Oaxaca to parents of Zapotec heritage. After his parents' death, he moved to Mexico City to live with an aunt. While he briefly attended the Academy of San Carlos, he was largely self-taught, feeling stifled by the academic traditions. In the post-revolutionary art scene dominated by the politically charged muralism of Rivera, Siqueiros, and Orozco, Tamayo chose a different path. He was more interested in formal and aesthetic concerns—color, texture, and form—than in overt political narrative. This stance often put him at odds with his contemporaries, who criticized his work as being "apolitical" or "Europeanized."</p>
                <h4>Artistic Style and International Recognition</h4>
                <p>Tamayo's genius lay in his ability to synthesize diverse influences. He drew inspiration from the vibrant colors of Mexican folk art, the abstract forms of pre-Columbian sculpture, and the innovations of European modernists like Picasso and Braque. He developed a style known as Mixografia, a printmaking technique that allowed for three-dimensional texture. His subjects were often universal and symbolic—figures, animals, and celestial bodies—rendered in rich, earthy tones and vibrant, almost electric, hues. He spent many years living and working in New York and Paris, which helped him achieve international recognition long before he was fully embraced by the Mexican art establishment.</p>
                <h4>Legacy of Universalism</h4>
                <p>Tamayo's legacy is that of a bridge-builder. He demonstrated that Mexican art could be both deeply rooted in its national identity and participate in a universal, international artistic dialogue. He believed that the plastic qualities of a painting were paramount, and his focus on color and form brought a new dimension to modern Mexican art. The Museo Tamayo Arte Contemporáneo in Mexico City, which houses his personal collection of international art, stands as a testament to his vision of a global artistic community.</p>
                <div class="quiz-container" data-correct="a">
                    <p class="quiz-question">Tamayo developed a unique printmaking technique that allowed for 3D texture called:</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-tamayo" value="a"> Mixografia</label>
                        <label><input type="radio" name="quiz-tamayo" value="b"> Muralism</label>
                        <label><input type="radio" name="quiz-tamayo" value="c"> Lithography</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>

            <h2 class="category-title">Film and Entertainment 🎬</h2>
            <div class="accordion">6. Guillermo del Toro (born 1964)</div>
            <div class="panel">
                <h4>Early Life and Love for Monsters</h4>
                <p>Born in Guadalajara, Guillermo del Toro developed a fascination with monsters and dark fantasy from a young age. He began making short films with his father's camera as a teenager. Raised in a strict Catholic household, he found himself drawn to the monstrous and the grotesque, often seeing them as more sympathetic than the human characters. He studied special effects and makeup with the legendary artist Dick Smith (The Exorcist) and spent nearly a decade running his own special effects company, Necropia, before directing his first feature film.</p>
                <h4>Directorial Style and Major Works</h4>
                <p>Del Toro's directorial debut was the stylish vampire horror film Cronos (1993). He later moved to Hollywood, but his experiences with studio interference on films like Mimic (1997) led him to alternate between big-budget American productions like Blade II and Hellboy, and more personal, Spanish-language films. His signature style is a blend of gothic horror, fairy tale, and historical drama. His films are visually spectacular, filled with intricate production design and a deep empathy for his "monsters." His masterpieces, The Devil's Backbone (2001) and Pan's Labyrinth (2006), are both set during the Spanish Civil War and use supernatural elements to explore the real-world horrors of fascism and war.</p>
                <h4>Academy Awards and Legacy</h4>
                <p>Del Toro achieved major mainstream success and critical acclaim with The Shape of Water (2017), a romantic fantasy about a mute janitor who falls in love with an amphibious creature. The film won four Academy Awards, including Best Picture and Best Director for del Toro. He also won an Oscar for his stop-motion animated film Pinocchio (2022). He is known as one of "The Three Amigos" of Mexican cinema, along with Alfonso Cuarón and Alejandro G. Iñárritu, a trio of directors who have achieved immense international success and critical recognition, elevating the profile of Mexican filmmaking on the global stage.</p>
                <div class="quiz-container" data-correct="c">
                    <p class="quiz-question">Which film won Guillermo del Toro the Academy Awards for Best Picture and Best Director?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-deltoro" value="a"> Pan's Labyrinth</label>
                        <label><input type="radio" name="quiz-deltoro" value="b"> Hellboy</label>
                        <label><input type="radio" name="quiz-deltoro" value="c"> The Shape of Water</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>
            
            <div class="accordion">7. Alfonso Cuarón (born 1961)</div>
            <div class="panel">
                <h4>Film School and Early Career</h4>
                <p>Alfonso Cuarón Orozco was born in Mexico City. He enrolled in the CUEC film school at the National Autonomous University of Mexico (UNAM), where he met many of his future collaborators, including cinematographer Emmanuel Lubezki. He was expelled from the school for making a short film in English. After working as a technician and assistant director in Mexican television and film, he made his feature directorial debut with the dark comedy Sólo con tu pareja (Love in the Time of Hysteria, 1991). The film's success at international festivals caught the attention of Hollywood producers.</p>
                <h4>Hollywood and International Success</h4>
                <p>In Hollywood, Cuarón directed diverse films like A Little Princess (1995) and a modern adaptation of Great Expectations (1998). His international breakthrough came with the critically acclaimed road movie Y tu mamá también (2001), a candid and provocative story of two teenage boys and an older woman on a journey through Mexico. The film earned him an Oscar nomination for Best Original Screenplay. He then directed the darkest and most critically lauded film in the Harry Potter series, Harry Potter and the Prisoner of Azkaban (2004).</p>
                <h4>Technical Mastery and Acclaim</h4>
                <p>Cuarón is renowned for his technical virtuosity, particularly his use of long, uninterrupted takes, which he and cinematographer Emmanuel Lubezki have perfected. This technique was on full display in the dystopian masterpiece Children of Men (2006) and the breathtaking space survival thriller Gravity (2013), for which he won his first Academy Award for Best Director. He won his second Best Director Oscar for Roma (2018), a deeply personal, black-and-white film based on his own childhood in the Roma neighborhood of Mexico City. The film was a love letter to the women who raised him and a poignant look at social class in 1970s Mexico. Cuarón is a filmmaker of immense range and vision, equally adept at intimate dramas and large-scale blockbusters.</p>
                <div class="quiz-container" data-correct="b">
                    <p class="quiz-question">Which deeply personal black-and-white film, based on his own childhood, earned Cuarón a Best Director Oscar?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-cuaron" value="a"> Gravity</label>
                        <label><input type="radio" name="quiz-cuaron" value="b"> Roma</label>
                        <label><input type="radio" name="quiz-cuaron" value="c"> Y tu mamá también</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>

            <div class="accordion">8. Salma Hayek (born 1966)</div>
            <div class="panel">
                <h4>From Telenovelas to Hollywood</h4>
                <p>Salma Hayek Pinault was born in Coatzacoalcos, Veracruz. She achieved stardom in Mexico in 1989 with the title role in the hit telenovela Teresa. Determined to pursue a Hollywood career, she moved to Los Angeles in 1991, despite speaking limited English and having dyslexia. She faced significant challenges and racism in an industry that offered few substantive roles for Latina actresses. Her big break came when director Robert Rodriguez cast her opposite Antonio Banderas in Desperado (1995).</p>
                <h4>Acting and Producing Career</h4>
                <p>Throughout the 1990s and 2000s, Hayek starred in a variety of films, including From Dusk till Dawn, Wild Wild West, and Dogma. Her most significant personal project was the 2002 biopic Frida. For years, she passionately pursued the film, eventually co-producing it and starring as Frida Kahlo. The role earned her nominations for an Academy Award, a Golden Globe, and a BAFTA for Best Actress. This project transformed her career, establishing her as a serious actress and a capable producer. Through her production company, Ventanarosa, she has produced projects like the Emmy-winning TV show Ugly Betty.</p>
                <h4>Advocacy and Impact</h4>
                <p>Salma Hayek has used her platform to advocate for women's rights and to fight against domestic violence and discrimination. She has been a vocal participant in the #MeToo movement, sharing her own experiences of harassment. By pushing for more complex roles and taking control of her own projects, she has opened doors for a new generation of Latino actors in Hollywood and has become one of the most visible and influential Latina figures in the global entertainment industry.</p>
                <div class="quiz-container" data-correct="c">
                    <p class="quiz-question">Starring in which 2002 biopic earned Salma Hayek an Academy Award nomination for Best Actress?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-hayek" value="a"> Desperado</label>
                        <label><input type="radio" name="quiz-hayek" value="b"> Ugly Betty</label>
                        <label><input type="radio" name="quiz-hayek" value="c"> Frida</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>
            
            <div class="accordion">9. Gael García Bernal (born 1978)</div>
            <div class="panel">
                <h4>An Actor from Birth</h4>
                <p>Born in Guadalajara to actor parents, Gael García Bernal began his acting career almost as soon as he could walk, appearing in telenovelas as a child. Seeking formal training, he moved to London to become the first Mexican accepted to study at the Central School of Speech and Drama. This classical training provided a foundation for the nuanced and powerful performances that would define his career.</p>
                <h4>The "Cinema Novo" and International Stardom</h4>
                <p>Bernal burst onto the international scene in 2000 with a stunning performance in Alejandro G. Iñárritu's critically acclaimed Amores perros. This was quickly followed by another global hit, Alfonso Cuarón's Y tu mamá también (2001), alongside his childhood friend Diego Luna. These two films announced the arrival of a vibrant new wave of Mexican cinema. Bernal's career has been defined by bold and often politically charged roles. He portrayed the young Che Guevara in The Motorcycle Diaries (2004), a priest with a dark secret in The Crime of Father Amaro (2002), and a transgender woman in Pedro Almodóvar's Bad Education (2004). He won a Golden Globe Award for his role as an eccentric orchestra conductor in the series Mozart in the Jungle.</p>
                <h4>Activism and Directing</h4>
                <p>Beyond acting, Bernal is a committed activist and filmmaker. He co-founded the production company Canana Films with Diego Luna, producing films that often explore social and political issues in Latin America. They also established the Ambulante documentary film festival, which travels to underserved communities in Mexico to make documentary cinema accessible to a wider audience. He has also stepped behind the camera, directing films like Déficit (2007) and Chicuarotes (2019). Bernal is more than just a movie star; he is a cultural force, using his art and influence to engage with the world around him.</p>
                <div class="quiz-container" data-correct="a">
                    <p class="quiz-question">With his friend Diego Luna, Bernal co-founded which traveling documentary film festival?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-bernal" value="a"> Ambulante</label>
                        <label><input type="radio" name="quiz-bernal" value="b"> Canana Films</label>
                        <label><input type="radio" name="quiz-bernal" value="c"> Mozart in the Jungle</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>

            <div class="accordion">10. Cantinflas (Mario Moreno) (1911-1993)</div>
            <div class="panel">
                <h4>The Man Who Mastered Gibberish</h4>
                <p>Mario Moreno Reyes, known to the world as Cantinflas, was born in a poor neighborhood in Mexico City. He tried various professions before finding his calling in traveling entertainment tents, or carpas. It was here that he developed his iconic character: a lovable, downtrodden peladito (a derogatory term for the urban poor, which he re-appropriated) with baggy pants, a tiny mustache, and a uniquely convoluted way of speaking. His speech was a masterful blend of non-sequiturs, double entendres, and gibberish, a style of talking that became so famous it was eventually officially recognized by the Royal Spanish Academy as the verb cantinflear: to talk a lot without saying anything of substance.</p>
                <h4>From the Tents to Cinematic Icon</h4>
                <p>His breakout film was Ahí está el detalle (There's the Rub, 1940). From that point on, he became the biggest star in the history of Mexican cinema. His character, Cantinflas, was a social critic disguised as a fool. He used his confusing language to satirize and outwit corrupt politicians, pompous intellectuals, and abusive bosses, always championing the cause of the common man. He became a national symbol, a representation of the ingenuity and resilience of the Mexican people.</p>
                <h4>Legacy and "The Mexican Chaplin"</h4>
                <p>Cantinflas's fame spread throughout the Spanish-speaking world. He made a successful foray into Hollywood with Around the World in 80 Days (1956), for which he won a Golden Globe. The legendary comedian Charlie Chaplin, after seeing one of his films, called him "the greatest comedian in the world." His legacy transcends cinema; he was a cultural phenomenon who gave a voice to the voiceless and proved that humor could be one of the most effective tools for social commentary.</p>
                <div class="quiz-container" data-correct="b">
                    <p class="quiz-question">His iconic style of speech led to which verb being added to the dictionary?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-cantinflas" value="a"> Chaplinear</label>
                        <label><input type="radio" name="quiz-cantinflas" value="b"> Cantinflear</label>
                        <label><input type="radio" name="quiz-cantinflas" value="c"> Morenear</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>
            
            <h2 class="category-title">Politics and Activism 🏛️</h2>
            <div class="accordion">11. Benito Juárez (1806-1872)</div>
            <div class="panel">
                <h4>From Humble Origins to National Leader</h4>
                <p>Benito Juárez was born into a poor, rural Zapotec family in Oaxaca and was orphaned at the age of three. He did not speak Spanish until he moved to Oaxaca City at age 12 to pursue an education. He initially studied for the priesthood but later earned a law degree and became a judge and governor of his state. His political career was defined by his unwavering commitment to liberalism, secularism, and the rule of law. As Minister of Justice, he was responsible for the Juárez Law (1855), which abolished the special legal privileges of the clergy and the military, a foundational step in establishing equality before the law.</p>
                <h4>The War of Reform and French Intervention</h4>
                <p>Juárez became president in 1858, leading the Liberal side in the bloody civil conflict known as the War of Reform against the Conservatives, who sought to maintain the power of the Catholic Church. After the Liberal victory, Mexico was financially ruined, forcing Juárez to suspend payment on foreign debts. This prompted an invasion by France, and in 1864, Napoleon III installed the Austrian archduke Maximilian von Habsburg as Emperor of Mexico. Juárez refused to recognize the monarchy and led a government in exile, waging a persistent guerrilla war. After five years of struggle, the French withdrew, Maximilian was executed, and Juárez triumphantly returned to Mexico City to restore the Republic.</p>
                <h4>Legacy of a National Hero</h4>
                <p>Juárez's presidency was instrumental in shaping modern Mexico. He championed the separation of church and state, public education, and the supremacy of civilian government. He remains Mexico's most revered national hero, a symbol of indigenous achievement, republican resistance to foreign imperialism, and unwavering principle. His famous maxim, "Entre los individuos, como entre las naciones, el respeto al derecho ajeno es la paz" ("Among individuals, as among nations, respect for the rights of others is peace"), is a guiding principle of Mexican foreign policy.</p>
                <div class="quiz-container" data-correct="c">
                    <p class="quiz-question">Juárez led the resistance against the imperial rule of which foreign-installed emperor?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-juarez" value="a"> Napoleon III</label>
                        <label><input type="radio" name="quiz-juarez" value="b"> Ferdinand VII</label>
                        <label><input type="radio" name="quiz-juarez" value="c"> Maximilian von Habsburg</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>
            
            <div class="accordion">12. Emiliano Zapata (1879-1919)</div>
            <div class="panel">
                <h4>Champion of the Southern Peasants</h4>
                <p>Emiliano Zapata Salazar was born in a rural village in the state of Morelos to a family of peasant farmers. From a young age, he witnessed the constant encroachment of large sugar plantations onto the communal lands of his village. He became a respected village leader and, in 1909, was elected to lead the defense of his community's land rights. When the Mexican Revolution broke out in 1910, Zapata saw an opportunity not just to overthrow the dictator Porfirio Díaz but to achieve fundamental agrarian reform. He quickly raised an army of peasant soldiers in the south, known as the Zapatistas.</p>
                <h4>The Plan of Ayala and Uncompromising Ideals</h4>
                <p>Zapata became disillusioned with the revolution's leader, Francisco Madero, whom he felt was not committed to land reform. In 1911, Zapata broke with Madero and issued his own revolutionary blueprint, the Plan of Ayala. This document called for the immediate and radical redistribution of land, demanding that one-third of all large hacienda lands be returned to the villages. His single-minded focus on "Tierra y Libertad" (Land and Liberty) made him an uncompromising and incorruptible figure in the revolution. He fought against every successive government that refused to implement his plan.</p>
                <h4>Martyrdom and Enduring Symbolism</h4>
                <p>The constant warfare took a toll on his home state of Morelos. In 1919, Zapata was lured into a trap and assassinated by government troops. His death was a devastating blow to the agrarian movement, but it transformed him into a martyr. Today, Zapata remains a potent international symbol of peasant resistance, agrarian struggle, and revolutionary integrity. His image and ideals were resurrected by the Zapatista Army of National Liberation (EZLN), an indigenous rights group that staged an uprising in Chiapas in 1994, ensuring that his fight for land and liberty continues to resonate.</p>
                <div class="quiz-container" data-correct="a">
                    <p class="quiz-question">What was the name of Emiliano Zapata's revolutionary blueprint demanding land reform?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-zapata" value="a"> Plan of Ayala</label>
                        <label><input type="radio" name="quiz-zapata" value="b"> Plan of San Luis Potosí</label>
                        <label><input type="radio" name="quiz-zapata" value="c"> Constitution of 1917</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>
            
            <div class="accordion">13. Pancho Villa (1878-1923)</div>
            <div class="panel">
                <h4>From Bandit to Revolutionary General</h4>
                <p>Born Doroteo Arango Arámbula, the man who would become Pancho Villa had a tumultuous early life. According to his own legend, he became an outlaw after shooting a wealthy hacienda owner who had assaulted his sister. He spent his youth as a cattle rustler and bandit in the mountains of Durango and Chihuahua. When the Mexican Revolution began in 1910, he saw an opportunity to use his skills for a larger cause. He joined Francisco Madero's movement and proved to be a brilliant and charismatic military leader.</p>
                <h4>The División del Norte and Military Genius</h4>
                <p>Villa's greatest achievement was the creation of the División del Norte (Division of the North), one of the most formidable and disciplined armies of the revolution. He was a master of cavalry tactics and logistics, using trains to move his troops and supplies with unprecedented speed. He financed his army by expropriating the vast estates of the wealthy landowners in the north. For a time, he was the most powerful man in Mexico, forming a brief alliance with Emiliano Zapata. Unlike the ideologically driven Zapata, Villa was more of a pragmatist, a populist who fought for the poor and sought to punish the rich.</p>
                <h4>The Columbus Raid and Legacy</h4>
                <p>After being defeated by his rival Venustiano Carranza, Villa's fortunes declined. In a controversial move in 1916, he led a raid on the border town of Columbus, New Mexico, killing several American citizens. The raid prompted the U.S. to send a Punitive Expedition led by General John J. Pershing into Mexico to hunt him down, a mission that ultimately failed. Villa eventually negotiated a pardon and retired to a ranch, but he was assassinated in 1923. He remains a complex and controversial figure: a folk hero to many, a ruthless bandit to others, but undeniably one of the most charismatic and influential leaders of the Mexican Revolution.</p>
                <div class="quiz-container" data-correct="b">
                    <p class="quiz-question">What was the name of Pancho Villa's famous and formidable revolutionary army?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-villa" value="a"> The Zapatistas</label>
                        <label><input type="radio" name="quiz-villa" value="b"> División del Norte</label>
                        <label><input type="radio" name="quiz-villa" value="c"> The Rurales</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>
            
            <div class="accordion">14. Sor Juana Inés de la Cruz (1648-1695)</div>
            <div class="panel">
                <h4>A Prodigy in a Man's World</h4>
                <p>Juana de Asbaje y Ramírez de Santillana, later known as Sor Juana, was a child prodigy born in colonial New Spain. She learned to read at the age of three and was soon devouring her grandfather's library. She pleaded with her mother to be allowed to disguise herself as a boy to attend the university. At the viceregal court in Mexico City, she astounded scholars with her vast knowledge. In an era when women had two acceptable life paths—marriage or the convent—Sor Juana chose the convent. It was not out of deep religious piety but because it was the only way she could continue her intellectual pursuits without the obligations of a husband and family.</p>
                <h4>The Convent as a Center of Learning</h4>
                <p>In the Convent of Saint Jerome, Sor Juana amassed a library of over 4,000 books (one of the largest in the Americas), collected scientific instruments, and wrote a stunning body of work, including poetry, plays, and theological treatises. Her poems are celebrated for their intellectual complexity, wit, and emotional depth, particularly her love poems, which challenged the patriarchal conventions of the time. Her most famous poem, "Hombres necios" ("Foolish Men"), is a blistering critique of the hypocrisy of men who condemn women for the very behavior they themselves encourage.</p>
                <h4>The "Reply" and Silencing</h4>
                <p>Sor Juana's brilliance and her willingness to engage in theological debate eventually drew the ire of the church hierarchy. After writing a private critique of a famous sermon, her work was published without her permission by the Bishop of Puebla, who then wrote to her under the pseudonym "Sor Filotea," admonishing her to focus on religious, not secular, studies. Sor Juana's response, La Respuesta a Sor Filotea de la Cruz (The Reply to Sor Filotea), is a passionate and autobiographical defense of a woman's right to education and intellectual life. It is considered by many to be the first feminist manifesto of the Americas. Under immense pressure, she eventually relinquished her books and instruments and rededicated herself to a life of penance. She died a few years later after contracting the plague while caring for her fellow sisters.</p>
                <div class="quiz-container" data-correct="c">
                    <p class="quiz-question">What is the title of Sor Juana's famous work defending a woman's right to education?</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-sorjuana" value="a"> Hombres necios</label>
                        <label><input type="radio" name="quiz-sorjuana" value="b"> The Divine Narcissus</label>
                        <label><input type="radio" name="quiz-sorjuana" value="c"> La Respuesta a Sor Filotea</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>

            <div class="accordion">15. Miguel Hidalgo y Costilla (1753-1811)</div>
            <div class="panel">
                <h4>The Unconventional Priest</h4>
                <p>Miguel Hidalgo was not a typical priest. Born to a well-off Creole family, he was a learned man, influenced by the Enlightenment ideas of the French Revolution. He was the rector of a prestigious seminary but was eventually sent to the small, poor town of Dolores after being investigated by the Inquisition for his unorthodox views. In Dolores, he was known more for his intellectual pursuits and his efforts to improve the economic fortunes of his parishioners—by teaching them to cultivate grapevines and silkworms—than for his piety.</p>
                <h4>The "Grito de Dolores"</h4>
                <p>In the early 1800s, resentment was growing among the Criollos (people of Spanish descent born in the Americas) against the peninsulares (Spanish-born colonists who held the top jobs). Hidalgo joined a literary club that was, in fact, a conspiracy plotting for independence from Spain, which had recently been conquered by Napoleon. When the conspiracy was discovered, Hidalgo decided to act immediately. In the early morning of September 16, 1810, he rang the church bells in Dolores, not to call his parishioners to mass, but to call them to rebellion. His speech, the "Grito de Dolores," was a passionate call to arms against bad government and the peninsulares.</p>
                <h4>The Father of Mexican Independence</h4>
                <p>Hidalgo's call unleashed a massive, violent, and largely undisciplined army of peasants and indigenous people, numbering in the tens of thousands. They marched under a banner of the Virgin of Guadalupe, Mexico's patron saint. Though he was a poor military strategist, Hidalgo's army had some initial successes. However, after a bloody campaign, his forces were defeated by the better-trained Spanish army. Hidalgo was captured, defrocked by the Inquisition, and executed by firing squad in 1811. Although he did not live to see Mexico become independent, his "Grito" is considered the spark that ignited the Mexican War of Independence. He is revered as the "Father of the Nation," and the anniversary of his cry is celebrated as Mexico's Independence Day.</p>
                <div class="quiz-container" data-correct="a">
                    <p class="quiz-question">Miguel Hidalgo's famous call to rebellion is known as the:</p>
                    <div class="quiz-options">
                        <label><input type="radio" name="quiz-hidalgo" value="a"> Grito de Dolores</label>
                        <label><input type="radio" name="quiz-hidalgo" value="b"> Plan of Iguala</label>
                        <label><input type="radio" name="quiz-hidalgo" value="c"> Sentiments of the Nation</label>
                    </div>
                    <button class="quiz-check-btn">Check Answer</button>
                    <p class="quiz-feedback"></p>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            // --- Global Score ---
            let score = 0;
            const scoreDisplay = document.getElementById('score-value');

            // --- Accordion Logic ---
            const accordions = document.querySelectorAll(".accordion");
            accordions.forEach(acc => {
                acc.addEventListener("click", function() {
                    this.classList.toggle("active");
                    const panel = this.nextElementSibling;
                    if (panel.style.maxHeight) {
                        panel.style.maxHeight = null;
                    } else {
                        panel.style.maxHeight = panel.scrollHeight + "px";
                    }
                });
            });

            // --- Theme Selector Logic ---
            const themeButtons = document.querySelectorAll('.theme-btn');
            themeButtons.forEach(button => {
                button.addEventListener('click', function() {
                    const theme = this.dataset.theme;
                    document.body.className = theme;
                    document.querySelector('.theme-btn.active').classList.remove('active');
                    this.classList.add('active');
                });
            });

            // --- UPDATED QUIZ LOGIC ---
            const quizCheckButtons = document.querySelectorAll('.quiz-check-btn');
            quizCheckButtons.forEach(button => {
                button.addEventListener('click', function() {
                    const quizContainer = this.closest('.quiz-container');
                    const selectedOption = quizContainer.querySelector('input[type="radio"]:checked');
                    const feedbackEl = quizContainer.querySelector('.quiz-feedback');
                    const correctAnswer = quizContainer.dataset.correct;
                    const radioButtons = quizContainer.querySelectorAll('input[type="radio"]');

                    // Disable all options and the button to prevent re-submission
                    radioButtons.forEach(radio => radio.disabled = true);
                    this.disabled = true;

                    if (!selectedOption) {
                        feedbackEl.textContent = "You didn't select an answer.";
                        feedbackEl.className = 'quiz-feedback incorrect';
                    } else if (selectedOption.value === correctAnswer) {
                        score++;
                        scoreDisplay.textContent = score;
                        feedbackEl.textContent = "Correct! +1 Point ✅";
                        feedbackEl.className = 'quiz-feedback correct';
                    } else {
                        feedbackEl.textContent = "Incorrect. The correct answer is highlighted.";
                        feedbackEl.className = 'quiz-feedback incorrect';
                    }

                    // Highlight the correct answer regardless
                    const correctLabel = quizContainer.querySelector(`input[value="${correctAnswer}"]`).parentElement;
                    correctLabel.classList.add('correct-answer');
                });
            });
        });
    </script>

</body>
</html>
"""

# ==============================================================================
# Python script to write the HTML file and generate the QR code.
# ==============================================================================
def create_webpage_and_qr_code():
    """
    Saves the HTML content to a file and generates a QR code pointing to it.
    """
    html_filename = "index.html"
    qr_code_filename = "webpage_final_quiz_qr.png"

    # 1. Write the HTML content to a file
    try:
        with open(html_filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✅ Successfully created webpage: {html_filename}")
    except IOError as e:
        print(f"❌ Error writing HTML file: {e}")
        return

    # 2. Get the absolute path to the HTML file and format it as a file URI
    public_url = "https://sohitpatel259.github.io/tourism_day/index.html"
    print(f"🔗 Webpage URI: {public_url}")

    # 3. Generate the QR code
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(public_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(qr_code_filename)
        print(f"✅ Successfully generated QR code: {qr_code_filename}")
        print("\n🎉 All done! Open the new HTML file and scan the new QR code.")
        
    except Exception as e:
        print(f"❌ Error generating QR code: {e}")

if __name__ == "__main__":
    create_webpage_and_qr_code()