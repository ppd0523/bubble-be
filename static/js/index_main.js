d3.json(URL.FILTER_API()).then(function(filter_objs){
    let cards = []
    let filter_ids = []
    filter_objs.forEach((obj, i, objs)=>{
        const filter_obj = obj;
        const report_api_url = URL.REPORT_API(filter_obj.filter_id, strfdate(new Date("2021-05-11")))

        async function fetchReport(){
            try{
                const report_objs = await d3.json(report_api_url);
                append_card(filter_obj, report_objs);
                filter_ids.push(filter_obj.filter_id)
                console.log(filter_obj.filter_id)

                // 카드가 다 채워지면 순서 정렬
                if(filter_ids.length == filter_objs.length){
                    d3.select(".container").selectAll(".card")
                    .data(filter_ids)
                    .sort()
                }
            }
            catch(error){
                console.log(error);
            }
        };
        fetchReport();
    });
});

function append_card(filter_obj, report_objs){
    
    // console.log(filter_obj.filter_id);
    let card = d3.select(".container")
        .append("div")
        .classed("card", true)
        .attr("data-filter-id", filter_obj.filter_id)
        .attr("margin-top", "0px")
    
        
    // title
    let title = card.append("div")
        .classed("title text", true)
        .style("position", "relative")
    
    // line
    title.append("hr")
        .attr("color", "#4d4d4d")
        .attr("size", 0)
        .attr("width", "95%")
        .attr("align", "center")
        
    title.append("h2")
        .text(filter_obj.filter_title)
        
    let g = title.append("svg")
        .style("position", "absolute")
        .style("right", "5px")
        .style("top", "2px")
        .attr("width", 32)
        .attr("height", 32)
        // .style("background-color", "white")
    // g.append("circle")
    //     .attr("cx", 32)
    //     .attr("cy", 32)
    //     .attr("r", 32)
    //     .attr("fill", "#4d4d4d")
    //     .attr("transform", "scale(0.5)")

    g.append("path")
        .attr("d", "M48 32 l-18 -18 M48 32 l-18 18 Z")
        .attr("stroke", "white")
        .attr("stroke-width", "6px")
        .attr("stroke-linecap", "round")
        .attr("transform", "scale(0.5)")
    
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
                .style("font-size", "1em")

    
    if(report_objs.length == 0){
        content.append("li")
        .style("color", "#4d4d4d")
        .style("font-weight", "bold")
        .text("없음")
    }
    else{
        content.selectAll("li")
        .data(report_objs)
        .join("li")
        .append("a")
        .attr("href", obj=>{return URL.STOCK_DETAIL(obj.stock_code, obj.stock_name)})
        .style("color", "#4d4d4d")
        .style("font-weight", "bold")
        .text(d=>d.stock_name)
    }
};
