import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http:HttpClient) { }

  getNfts(){
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('token')}`
    });
    return this.http.get('http://127.0.0.1:5000/getnfts', { headers: headers });
  }

  getTraderNfts(){
    const id = localStorage.getItem('id')
    return this.http.post('http://127.0.0.1:5000/getTraderNfts', {id: id});
  }

  transaction(amount: string, type: string){
    const id = localStorage.getItem('id')
    const amt = amount
    const typ = type 
    return this.http.post('http://127.0.0.1:5000/transaction', {id: id, amount: amt, type: typ});
  }

  getAllTrader_TransHistory(from:Date, to: Date){
    const id = localStorage.getItem('id')
    const fm_date = from
    const t_date = to
    return this.http.post('http://127.0.0.1:5000/getAllTrader_TransHistory', {id: id, from: fm_date, to: t_date});
  }

  getTTransHistory(){
    const id = localStorage.getItem('id')
    return this.http.post('http://127.0.0.1:5000/getTTransHistory', {id: id});
  }

}
