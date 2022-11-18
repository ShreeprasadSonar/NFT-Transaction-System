import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SellNftsComponent } from './sell-nfts.component';

describe('SellNftsComponent', () => {
  let component: SellNftsComponent;
  let fixture: ComponentFixture<SellNftsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SellNftsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SellNftsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
