import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {MainService} from './main.service';
import {ITask, ITasklist} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }

  getTasklists(): Promise<ITasklist[]> {
    return this.get('http://localhost:8000/api/task_lists/', {});
  }
  getTasks(task: ITasklist): Promise<ITask[]> {
    return this.get(`http://localhost:8000/api/task_lists/${task.id}/tasks/`, {});
  }
  createTaskList(n: any): Promise<ITasklist> {
    return this.post('http://localhost:8000/api/task_lists/', {
      name: n
    });
  }

  updateTaskList(tasklist: ITasklist): Promise<ITasklist> {
    return this.put(`http://localhost:8000/api/task_lists/${tasklist.id}/`, {
      name: tasklist.name
    });
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_lists/${id}/`, {});
  }
}
