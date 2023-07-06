if __name__ == "__main__":
    
    # input_start()
    search = "나비"

    naver_urls = ['https://sports.news.naver.com/news.nhn?oid=442&aid=0000163350', 'https://n.news.naver.com/mnews/article/001/0014045673?sid=103', 'https://n.news.naver.com/mnews/article/366/0000913600?sid=101', 'https://n.news.naver.com/mnews/article/025/0003290622?sid=102']

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}

    titles = []
    contents = []

    for url in naver_urls:
        orginial_html = requests.get(url, headers=headers)
        html = BeautifulSoup(orginial_html.text, "html.parser")

        title = html.select("div#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
        title = ''.join(str(title))

        pattern1 = r'<[^>]*>'
        title = re.sub(pattern=pattern1, repl='', string=title)
        titles.append(title)

        content = html.select("div#dic_area")
        content = ''.join(str(content))
        content = re.sub(pattern=pattern1, repl='', string=content)
        pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
        content = content.replace(pattern2,  '')
        contents.append(content)

print(titles)
print(contents)

news_df = pd.DataFrame({'title':titles, 'link': naver_urls, 'content': contents})
news_df.to_csv(f'NaverNews_{search}.csv', index=False,  encoding='utf-8')