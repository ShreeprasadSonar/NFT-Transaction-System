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

  addEth(){
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('token')}`,
      amount: "10",
      type: "ETH",
      t_id: "897982743423423",
      t_date_time: "25/06/2022 12 PM",
      status: "Active"
    });  
    return this.http.get('http://127.0.0.1:5000/transaction', { headers: headers });
  }
//example
  getTraderNfts(){
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('token')}`,

    });  
    return this.http.get('http://127.0.0.1:5000/getTraderNfts', { headers: headers });
  }

  //example2

  transaction(){
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('token')}`,
      amount: "10",
      type: "ETH",
      t_id: "897982743423423",
      t_date_time: "25/06/2022 12 PM",
      status: "Active"
    });  
    return this.http.get('http://127.0.0.1:5000/transaction', { headers: headers });
  }


}
