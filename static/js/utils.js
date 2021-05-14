function strfdate(date){
    let year = date.getFullYear()
    let month = (1 + date.getMonth())
    month = month >= 10 ? month : '0' + month
    let day = date.getDate()
    day = day >= 10 ? day : '0' + day
    return year + '-' + month + '-' + day
}

let URL = {
    FILTER_API : (filter_id)=>{
        let url = "/api/filter/"
        if (filter_id) url += `${filter_id}/`;
        return url
    },
    REPORT_API : (filter_id, date)=>{
        let url = "/api/filter/"
        if (filter_id && date) url += `${filter_id}/report/${date}/`
        return url
    },
    STOCK_PRICE_API : (stock_code)=>{
        `/api/stock/${stock_code}/price/`
        let url = "/api/stock/"
        if (stock_code) url += `${stock_code}/price/`
        return url
    },
    FILTER_DETAIL : (filter_id)=>{
        let url = "/filter/"
        if (filter_id) url += `?filter_id=${filter_id}`;
        return url
    },
    STOCK_DETAIL : (stock_code, stock_name)=>{
        let url = "/stock/"
        if(stock_code && stock_name) url += `?stock_code=${stock_code}&stock_name=${stock_name}`;
        return url
    },
}