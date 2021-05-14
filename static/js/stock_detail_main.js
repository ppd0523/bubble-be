let params = new URLSearchParams(location.search);
let stock_code = params.get("stock_code");
let stock_name = params.get("stock_name");

let container = d3.select(".container")

container.append("h2")
.classed("title", true)
.classed("text", true)
.text(stock_name)

d3.json(URL.STOCK_PRICE_API(stock_code)).then(function(price_objs){
    console.log(price_objs);
    container.append("div")
    .selectAll("p")
    .data(price_objs)
    .join("p")
    .text(obj=>obj.adj_close_price)
    .classed("text", true)
});