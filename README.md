# 🏨 Hotel Booking & Spa Reservation System
This project is a comprehensive hotel reservation application designed to demonstrate advanced Object-Oriented Programming (OOP) principles in Python. The system allows users to search for hotels, process secure card payments, and optionally book spa services.

## 🛠️ Installation & Setup
Clone the repository (or copy the project files).

Install requirements: This project uses pandas for data management.

Bash

pip install pandas
Data Files: Ensure the following CSV files are in the root directory:

hotels.csv - Hotel database.

cards.csv - Payment card database.

card_security.csv - 2FA password database.

## 🚀 Key Features
Hotel Management: Reading data from CSV, availability checks, and persistent booking updates.

Secure Payment Gateway: Two-factor authentication (data validation + password) via class inheritance.

Spa Packages: Specialized SpaHotel type with extended service offerings.

Automatic Confirmation: Generation of text-based tickets for different service types.

## 🏗️ OOP Concepts Applied
Inheritance: SpaHotel inherits from Hotel; SecureCreditCard inherits from CreditCard.

Method Overriding: Customizing parent methods in subclasses.

Composition: Linking ReservationTicket to Hotel objects without inheritance.

Encapsulation: Managing data access through Pandas and structured classes.

Abstract Base Classes (ABC): Structuring code via templates (as discussed in theoretical parts).

Magic Methods: Customizing object behavior (e.g., __eq__ for ID-based comparison).

# 🏨 Systém pro rezervaci hotelů a SPA
Tento projekt je komplexní aplikací pro rezervaci hotelů, navrženou pro demonstraci pokročilých principů objektově orientovaného programování (OOP) v Pythonu. Systém umožňuje uživatelům vyhledávat hotely, provádět bezpečné platby kartou a volitelně si objednávat lázeňské služby.

## 🛠️ Instalace a nastavení
Naklonujte repozitář (nebo zkopírujte soubory projektu).

Nainstalujte potřebné knihovny: Projekt využívá pandas pro správu dat.

Bash

pip install pandas
Datové soubory: Ujistěte se, že v kořenovém adresáři jsou následující soubory CSV:

hotels.csv - Databáze hotelů.

cards.csv - Databáze platebních karet.

card_security.csv - Databáze hesel pro 2FA.

## 🚀 Klíčové funkce
Správa hotelů: Načítání dat z CSV, kontrola dostupnosti a trvalý zápis rezervací.

Bezpečná platební brána: Dvoufázové ověření (validace údajů + heslo) pomocí dědičnosti tříd.

SPA balíčky: Specializovaný typ SpaHotel s rozšířenou nabídkou služeb.

Automatické potvrzení: Generování textových jízdenek pro různé typy služeb.

## 🏗️ Použité OOP koncepty
Dědičnost (Inheritance): SpaHotel dědí z Hotel; SecureCreditCard dědí z CreditCard.

Přepisování metod (Overriding): Úprava metod rodiče v dceřiných třídách.

Kompozice: Propojení ReservationTicket s objekty Hotel bez nutnosti dědičnosti.

Zapouzdření (Encapsulation): Řízení přístupu k datům skrze Pandas a strukturované třídy.

Abstraktní třídy (ABC): Strukturování kódu pomocí šablon (probíráno v teoretické části).

Magické metody: Úprava chování objektů (např. __eq__ pro porovnávání na základě ID).