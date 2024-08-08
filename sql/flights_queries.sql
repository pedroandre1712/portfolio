/* Selecione os diferentes anos das datas de chegadas (flights.scheduled_arrival) dos voos */
select distinct extract (YEAR FROM scheduled_arrival) FROM bookings.flights;

/* Selecione os diferentes meses das datas de partida (flights.scheduled_departure) dos voos*/
select distinct extract (MONTH FROM scheduled_departure) FROM bookings.flights;

/* Apresente o nome das diferentes tipos de classes de voo (ticket_flights.fare_conditions)
 com todos os caracteres em minusculo */
select distinct lower(ticket_flights.fare_conditions) from bookings.ticket_flights;

/* Apresente o dia, mês e ano dos voos de chegada separadas for hífen em uma única coluna */
select concat(extract(day from scheduled_arrival), '-',  extract(month from scheduled_arrival),'-', extract(year from scheduled_arrival)) from bookings.flights;

/* selecione o numero de voos de chegada que ocorreram por dia e apresente-os de maneira em que os dias
que tiveram mais voos de chegada aparecam primeiro */
select extract(day from scheduled_arrival), count(flight_no) from bookings.flights
group by extract(day from scheduled_arrival)
order by count(flight_no) desc;

/* Apresente o número máximo de voos de chegada que cada aeroporto recebeu por dia */
select arrival_airport, count(flight_no) from bookings.flights 
group by arrival_airport
order by count(flight_no) desc
limit 1;

select * from bookings.flights;

/* Apresente o numero de vezes em que cada assento foi escolhido pelo nome do passageiro que mais comprou tickets */
select bbp.seat_no , count(bbp.seat_no) from bookings.boarding_passes bbp
inner join bookings.ticket_flights btf ON btf.ticket_no = bbp.ticket_no
inner join bookings.tickets bt ON bt.ticket_no = bbp.ticket_no
where bt.passenger_name = (SELECT tickets.passenger_name 
						   from bookings.tickets 
						   group by passenger_name 
						   order by count(tickets.ticket_no) desc 
						   limit 1)
group by bbp.seat_no
order by count(passenger_name) desc;
