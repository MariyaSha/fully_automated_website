const articles = $input.first().json.data;

if (!articles.some(
  article => article.link === $('Edit Fields').first().json.link
)) {

articles.unshift({
  title: $('Edit Fields').first().json.title,
  contentSnippet: $('Basic LLM Chain1').first().json.text,
  source: "Tech Goblin",
  link: $('Edit Fields').first().json.link,
  pubDate: new Date().toISOString()
});
}

return articles.map(json => ({ json }));
