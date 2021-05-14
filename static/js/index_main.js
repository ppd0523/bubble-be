let FILTER_API_URL = "api/filter/"
let STOCK_PRICE_API_URL = "api/stock/price/"

d3.json(FILTER_API_URL).then(function(filters){
    filters.forEach((obj, i, objs)=>{
        let REPORT_URL = `${FILTER_API_URL}${obj.filter_id}/report/${strfdate(new Date("2021-05-13"))}`;
        let filter_obj = obj;
        d3.json(REPORT_URL).then(function(report_objs){
            // console.log(`${filter_obj.filter_id}`)
            append_card(filter_obj, report_objs);
            // console.log(reports);
        });
    })
});

function append_card(filter_obj, report_objs){
    let card = d3.select(".container").append("div").classed("card", true)
    card.append("hr");
    
    let title = card.append("div")
    title.classed("title", true)
    .classed("text", true)
    .append("h2")
    .text(filter_obj.filter_title)
    .on("click", ()=>{
        // 조건식 결과 상세 페이지 링크
        // location.href = FILTER_DETAIL_URL + data['condition_name']
    })

    let content = card.append("div")
    content.classed("content", true)
    .classed("text", true)
    .append("ul")
    .selectAll("li")
    .data(report_objs)
    .join("li")
    .append("a")
    .attr("href", d=>{return `${STOCK_PRICE_API_URL}${d.stock_code}`})
    .text(d=>d.stock_name)
};


