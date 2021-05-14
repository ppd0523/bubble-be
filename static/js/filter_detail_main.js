let params = new URLSearchParams(location.search);
let filter_id = params.get("filter_id");

let container = d3.select(".container")

container.append("h2")
.classed("title", true)
.classed("text", true)

d3.json(URL.FILTER_API(filter_id)).then(function(filter_obj){
    d3.select(".title")
    .text(filter_obj.filter_title)
});


d3.json(URL.REPORT_API(params.get("filter_id"), strfdate(new Date("2021-05-11")))).then(function(report_objs){
    report_objs.forEach((obj, i, objs)=>{
        append_chart(obj);
        // console.log(obj);
    })
});

function append_chart(report_obj){
    // header
    let chart = container.append("div")
    .classed("chart text", true)
    
    // title
    chart.append("div")
    .classed("title noselect", true)
    .append("p")
    .append("a")
    .attr("href", URL.STOCK_DETAIL(report_obj.stock_code, report_obj.stock_name))
    .text(report_obj.stock_name)
    
    // content
    chart.append("div")
    .classed("content", true)
    .append("p")
    
}

