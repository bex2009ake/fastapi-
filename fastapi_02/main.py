from fastapi import FastAPI, HTTPException
from aaa import aaa
import uvicorn
from schemas import *


app = FastAPI(title='Fastapi tutorial 02')
posts = []


@app.get('/read')
async def read_post():
    return {'data': posts}


@app.post('/create')
async def create_post(post: Post):
    posts.append(post.__dict__)

    return { 'data': post.__dict__ }


@app.put('/edit/{post_id}')
async def edit_post(post_id: int, post: Post):
    for i, val in enumerate(posts):
        if val['id'] == post_id:
            posts[i] = post
            return { 'data': post.__dict__ }
    raise HTTPException(status_code=404, detail='Not Found')


@app.delete('/delete/{post_id}')
async def delete_post(post_id: int):
    for i, val in enumerate(posts):
        if val['id'] == post_id:
            posts.pop(i)
            return {'msg': 'Deleted'}
    raise HTTPException(status_code=404, detail='Not Found')

@app.get('/detail/{post_id}')
async def detail_post(post_id: int):
    for i, val in enumerate(posts):
        if val['id'] == post_id:
            return { 'data': val }
    raise HTTPException(status_code=404, detail='Not Found')

if __name__ == '__main__':
    uvicorn.run('main:app', port=5050, reload=True)