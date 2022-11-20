import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BuynftComponent } from './buynft.component';

describe('BuynftComponent', () => {
  let component: BuynftComponent;
  let fixture: ComponentFixture<BuynftComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BuynftComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BuynftComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
