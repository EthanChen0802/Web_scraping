from selenium import webdriver
import time
import pprint

def get_movie_data():
    print('please type the movie you want to search on imdb')
    search_movie_title = str(input())


    movie_title_xpath = "//h1"
    movie_poster_xpath = "//div[@class='poster']/a/img"
    movie_rating_xpath = "//strong/span"
    movie_genre_xpath ="//div[@class='subtext']/a"
    movie_cast_xpath = "//td[2]/a"
    imdb_search_input_xpath = "//input[@id='suggestion-search']"
    imdb_search_button_xpath = "//button[@id='suggestion-search-button']"
    imdb_search_movie_xpath = "//ul[@class='findTitleSubfilterList']/li[1]/a"
    imdb_search_result_xpath = "//td[@class='result_text']/a"


    # Use Chrome瀏覽器
    driver_path = "C:/Users/User/Desktop/chromedriver.exe"  
    imdb_home = "https://www.imdb.com/"                                      
    driver = webdriver.Chrome(executable_path=driver_path)  
    driver.get(imdb_home)

    # Search movie title
    elem = driver.find_element_by_xpath(imdb_search_input_xpath)
    elem.send_keys(search_movie_title)

    elem = driver.find_element_by_xpath(imdb_search_button_xpath)
    elem.click()


    # Filter search results to 'movie category'
    time.sleep(5)
    elem = driver.find_element_by_xpath(imdb_search_movie_xpath)
    elem.click()


    # Click most relevant result (first result)
    time.sleep(5)
    elems = driver.find_elements_by_xpath(imdb_search_result_xpath)
    first_elem = elems[0]
    first_elem.click()


    # Movie title
    time.sleep(5)
    elem = driver.find_element_by_xpath(movie_title_xpath)
    movie_title = elem.text

    # Movie poster
    elem = driver.find_element_by_xpath(movie_poster_xpath)
    movie_poster = elem.get_attribute('src')

    # Movie rating
    elem = driver.find_element_by_xpath(movie_rating_xpath)
    movie_rating = elem.text

    # Movie genre
    elem = driver.find_elements_by_xpath(movie_genre_xpath)
    movie_genre = [i.text for i in elem]
    movie_release_date = movie_genre.pop()
        
    # Movie cast
    elem = driver.find_elements_by_xpath(movie_cast_xpath)
    movie_cast = [i.text for i in elem]


    movie_data = {
        'movieTitle': movie_title,
        'moviePoster': movie_poster, 
        'movieRating': movie_rating,
        'movieGenre': movie_genre,
        'movieCast': movie_cast
    }

    return movie_data


movie = get_movie_data()
pprint.pprint(movie)