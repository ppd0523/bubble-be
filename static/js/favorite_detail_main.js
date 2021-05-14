let params = new URLSearchParams(location.search);
let filter_id = params.get("filter_id");

d3.json(URL.FILTER_API(filter_id)).then(function(filter_obj){
    d3.select(".title")
    .text(filter_obj.filter_title)
});


d3.json(URL.REPORT_API(params.get("filter_id"), strfdate(new Date("2021-05-11")))).then(function(reports){
    console.log(reports);
});

d3.select(".container")
.append("h2")
.classed("title", true)
.classed("text", true)

console.log(`${params.get("filter_id")}`)