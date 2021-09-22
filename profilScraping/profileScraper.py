def isMatch(string, sub_str):
    if (string.find(sub_str) == -1):
        return False
    else:
        return True

def scrapData(url):
    import requests
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    # driver.get("https://in.pinterest.com/")
    driver.get(url)

    profileName = driver.find_element_by_xpath("//div[@class='Whs(nw) Ovx(h) Tov(e) Maw(100%) Fz($fzbutton) Fw($fwbutton) Lh($lhbody) C($darkText)']").text
    profileHandle = driver.find_element_by_xpath("//span[@class='Whs(nw) Ovx(h) Tov(e) Maw(100%)']").text
    profileIcon = driver.find_element_by_xpath("//div[@class='Pos(a) W($8xl) H($8xl) TranslateY(-33%) Bdrs(50%) Bgc($white2) Bgz(cv) Bgr(nr) Bgp(c_t) Bd($bddp)']").value_of_css_property('background-image')
    tagLine = driver.find_element_by_xpath("//div[@class='Py($sm) Mb($xxs) Fw($fwcaption) C($secondaryDark) Fz($fzbutton) Lh($lhmediumCaption) Ta(c)']").text
    followers = None
    following = None

    hrefs = []
    pattern1 = "follower"
    pattern2 = "following"
    followDetails = driver.find_elements_by_tag_name('a')
    for tag in followDetails:

        src = (tag.get_attribute('href'))
        # print(src)
        if isMatch(src, pattern1):  # for followers count
            if followers is None:
               childrens = tag.find_elements_by_xpath(".//*")
               followers = (childrens[0].text)
            hrefs.append(src)
        if isMatch(src, pattern2):  # for following count
            childrens = tag.find_elements_by_xpath(".//*")
            print(childrens[0].text)
            hrefs.append(src)

    # print(profileHandle,profileIcon,profileName,following,followers)

    profile ={'profileName':profileName,'profileHandle':profileHandle,'profileIcon':profileIcon,'tagLine':tagLine,'followers':followers}
    print(profile)
    r = requests.post(url="http://localhost:8080/add", json={
        "profileName": profileName,
        "profileHandle": profileHandle,
        "profileIconUrl": profileIcon,
        "tagline": tagLine,
        "followers": followers
    })
    print(r.status_code)
    print(r.text)



# //1)
# python script
# 2) kafka consumer
#     ->



# 1) PYTHON Scpt. ->> go server post request(profile link) ->kafka producer->python script no 2 (consume data)->scape data -> go server (post) -> db persist
