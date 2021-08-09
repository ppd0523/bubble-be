import pandas as pd


def groupby_data(queryset: list) -> list:
    df = pd.DataFrame(list(queryset.values()))
    df.drop(columns=['stock_code', 'stock_name', 'id'], inplace=True)
    df['create_date'] = pd.to_datetime(df['create_date'])  # datetime

    ddf = df.copy()
    ddf['create_date'] = ddf['create_date'].apply(lambda x: x.strftime('%Y-%m-%d'))

    wdf = _grouping(df, 'W')
    wdf = wdf.reset_index().rename(columns={'index': 'create_date'})
    wdf['create_date'] = wdf['create_date'].apply(lambda x: x.strftime('%Y-%m-%d'))

    mdf = _grouping(df, 'M')
    mdf = mdf.reset_index().rename(columns={'index': 'create_date'})
    mdf['create_date'] = mdf['create_date'].apply(lambda x: x.strftime('%Y-%m-%d'))

    return ddf.to_json(orient='records'), wdf.to_json(orient='records'), mdf.to_json(orient='records')


def _grouping(df, freq):
    return df.groupby(pd.Grouper(key='create_date', freq=freq)).agg(
        high_price=pd.NamedAgg(column='high_price', aggfunc='max'),
        low_price=pd.NamedAgg(column='low_price', aggfunc='min'),
        open_price=pd.NamedAgg(column='open_price', aggfunc='first'),
        close_price=pd.NamedAgg(column='close_price', aggfunc='last'),
        adj_close_price=pd.NamedAgg(column='adj_close_price', aggfunc='last'),
        volume=pd.NamedAgg(column='volume', aggfunc='sum'),
    )