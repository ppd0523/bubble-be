d3.json(URL.FILTER_API()).then(function(filter_objs){
    // filter_objs.sort((a, b)=>{return (a.filter_id < b.filter_id)? -1: 1;});
    // console.log(filter_objs);
    filter_objs.forEach((obj, i, objs)=>{
        let filter_obj = obj;
        let report_api_url = URL.REPORT_API(filter_obj.filter_id, strfdate(new Date("2021-05-11")))

        d3.json(report_api_url).then(function(report_objs){
            append_card(filter_obj, report_objs);
        });
    })
});

function append_card(filter_obj, report_objs){
    
    // console.log(filter_obj.filter_id);
    let card = d3.select(".container")
    .append("div")
    .classed("card", true)
    .attr("data-filter-id", filter_obj.filter_id)
    
    // line
    card.append("hr");
    
    // title
    let title = card.append("div")
                .classed("title text", true)
                .append("h2")
                .text(filter_obj.filter_title)
    
    if(report_objs.length > 0){
        title.on("click", ()=>{
            // 조건식 결과 상세 페이지 링크
            location.href = URL.FILTER_DETAIL(filter_obj.filter_id)
        })
    }

    // content
    let content = card.append("div")
                .classed("content text", true)
                .append("ul")
    
    if(report_objs.length == 0){
        content.append("li")
        .classed("text", true)
        .style("font-size", "0.8em")
        .text("없음")
    }
    else{
        content.selectAll("li")
        .data(report_objs)
        .join("li")
        .append("a")
        .classed("text", true)
        .style("font-size", "0.8em")
        .attr("href", obj=>{return URL.STOCK_DETAIL(obj.stock_code, obj.stock_name)})
        .text(d=>d.stock_name)
    }
};


