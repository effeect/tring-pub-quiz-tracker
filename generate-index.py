from jinja2 import Template

template = """
<html>
<head>
<title>{{ title }}</title>
</head>
<body>
<h1>{{ headline }}</h1>
<p>{{ content }}</p>
</body>
</html>
"""

template = Template(template)

output = template.render(title="My Title", headline="My Headline", content="My Content")
print(output)

