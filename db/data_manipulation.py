from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.User import User
from db.UsersNote import UsersNote

async def create_user (session : AsyncSession , user_data) :
    
    result  = await session.execute(select(User).where(User.username == user_data.username, 
                                       User.password == user_data.password))
    
    user = result.scalar_one_or_none()

    if not user :
        
        session.add(User(
            username = user_data.username,
            password = user_data.password,
            email = user_data.email   
        ))
        
        return {
            "message" : "Добавил в бд"
        }
        
async def user_verification (session : AsyncSession , users_data) :
    
    result = await session.execute(select(User).where(User.username == users_data.username,
                                                      User.password == users_data.password))
    user = result.scalar_one_or_none()
    
    if user :
        return {
            "user_id": user.id,
            "username": user.username 
        }
    
async def create_user_task (session : AsyncSession , user_id , user_task_data):
    
    for task in user_task_data :
        session.add(UsersNote(
            user_id = user_id,
            title = task.title,
            description = task.description
        ))
        
    await session.commit()
    return {
        "message" : "Ваши задачи добавлены в бд!"
    }

async def get_users_task (session : AsyncSession , user_id , filtering_by_title = None):
    
    query = select(UsersNote).where(UsersNote.user_id == user_id)
    
    if filtering_by_title :
        
        query = query.where(UsersNote.title.contains(filtering_by_title))
    
    result = await session.execute(query)
    
    return result.scalars().all()

async def delete_tasks (session : AsyncSession , user_id , task_id) :
    
    result = await  session.execute(select(UsersNote).where(UsersNote.user_id == user_id,
                                                     UsersNote.id == task_id 
                                                     ))
    task = result.scalar_one_or_none()
    
    if task :
        
        await session.delete(task)
        await session.commit()
        
        return {
            "message" : "Ваша задачу успещно удолена"
        }

async def update_tasks (session : AsyncSession , user_id , task_id , updated_data) :
    result = await session.execute(select(UsersNote).where(UsersNote.user_id == user_id,
                                                     UsersNote.id == task_id
                                                     ))
    task = result.scalar_one_or_none()
    
    if task :
        task.title = updated_data.title
        task.description = updated_data.description
        await session.commit()
        
        await session.refresh(task)
        
        return {
            "message" : "Ваши данные обновлены",
            "updated_task" : {
                "title" : task.title,
                "description" : task.description
            }
        }
        
async def completed_tasks (session : AsyncSession , user_id , task_id) :
    result = await session.execute(select(UsersNote).where(UsersNote.user_id == user_id,
                                                     UsersNote.id == task_id
                                                     ))
    task = result.scalar_one_or_none()
    
    if task  :
        
        task.completed = True
        await session.commit()
        return {
            "message" : "✅✅✅✅✅"
        }