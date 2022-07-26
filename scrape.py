import os
import re
import requests
import sys
from bs4 import BeautifulSoup
from course_links import course_links
from common_mime import common_mime
from headers import headers, cookies

visited_urls = set()

def download_content(url, cur_path, ignore_course_menu=True, verbose=True):

	if url in visited_urls:
		return

	if verbose:
		print(cur_path)

	os.makedirs(cur_path, exist_ok=True)

	visited_urls.add(url)

	response = requests.get(url, headers=headers,
							cookies=cookies, allow_redirects=True)

	soup = BeautifulSoup(response.content, 'html.parser')

	with open(os.path.join(cur_path, 'page.html'), "w") as f:
		f.write(str(soup))

	if ignore_course_menu:
		soup = soup.find("div", {"id": "content"})

	if soup is None:
		return


	for link in soup.find_all('a'):
		if link.has_attr('href'):
			href = link['href']
		else:
			continue
		
		name = " ".join(link.get_text().split())
		name = re.sub('/', '', name)
		
		if href.startswith('/webapps/blackboard/content/listContent'):
			if href.endswith('logout'):
				continue
			download_content(
				f"https://online.manchester.ac.uk{href}", os.path.join(cur_path, name))

		if href.startswith('/bbcswebdav'):
			download_file(f"https://online.manchester.ac.uk{href}", cur_path, name)

		if href.startswith('https://online.manchester.ac.uk/bbcswebdav'):
			download_file(href, cur_path, name)


def download_file(url, path, name):
	if url in visited_urls:
		return

	visited_urls.add(url)

	response = requests.get(url, headers=headers, cookies=cookies)

	content_type = response.headers.get('content-type')

	if content_type.startswith('application'):
		extension = common_mime[content_type]
		if os.path.exists(os.path.join(path, f'{name}{extension}')):
			for i in range(1, 100):
				if os.path.exists(os.path.join(path, f'{name} ({i}){extension}')):
					continue

				name = f'{name} ({i})'
				break

		
		print(f'{path}/{name}{extension}')

		with open(os.path.join(path, f'{name}{extension}'), 'wb') as f:
			f.write(response.content)


if __name__ == "__main__":
	if len(sys.argv) > 1:
		path = sys.argv[0]
	else:
		path = 'University'
	for name, link in course_links.items():
		print(f'Downloading {name}...')
		download_content(link, os.path.join(path, name), ignore_course_menu=False)
