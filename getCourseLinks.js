(() => {
	var links = {}
	var tabs = ['CurrentCourses', 'FormerCourses'] 
	tabs.forEach(tab => {
		var items = document.getElementById(tab).querySelector("ul").querySelectorAll("li")
		items.forEach(item => {
			a = item.querySelector('a')
			links[a.innerHTML] = a.href
		});
	});
		
	console.log(links)
	
})()

