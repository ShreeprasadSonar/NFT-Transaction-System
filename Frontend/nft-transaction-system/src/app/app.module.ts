import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { HomepageComponent } from './homepage/homepage.component';
import { HeaderComponent } from './header/header.component';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SignupComponent } from './signup/signup.component';
import { TradeComponent } from './trade/trade.component';

import { SearchFilterPipe } from './search-filter.pipe';
import { ManagerDashboardComponent } from './manager-dashboard/manager-dashboard.component';
import { SellNftsComponent } from './sell-nfts/sell-nfts.component';
import { TransactionsComponent } from './transactions/transactions.component';
import { AddmoreComponent } from './addmore/addmore.component';
import { CancelComponent } from './cancel/cancel.component';
import { BuynftComponent } from './buynft/buynft.component';


@NgModule({
  declarations: [
    AppComponent,
    HomepageComponent,
    HeaderComponent,
    LoginComponent,
    DashboardComponent,
    SignupComponent,
    TradeComponent,
    SearchFilterPipe,
    ManagerDashboardComponent,
    SellNftsComponent,
    TransactionsComponent,
    AddmoreComponent,
    CancelComponent,
    BuynftComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
