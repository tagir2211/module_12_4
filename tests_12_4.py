import unittest
import logging
import runner


class RunnerTest(unittest.TestCase):
    is_frizen = False

    def test_walk(self):
        '''
        Test class Runner, functoin walc
        :return:
        '''
        try:
            t_walk = runner.Runner(563,)
            logging.info('Экземпляр класса Runner создан успешно', exc_info=True)
        except TypeError as er_T:
            logging.warning('Экземпляр класса Runner не создан, задано неверное имя', exc_info=True)
            
        for _ in range(1, 11):
            try:
                t_walk.walk()
                logging.info('"test_walk" выполнен успешно', exc_info=True)
            except:
                logging.warning('Неверная скорость для Runner', exc_info=True)
        self.assertEqual(t_walk.distance, 50)

   
    def test_run(self):
        '''
        Test class Runner, functoin run
        :return:
        '''
        try:
            t_run = runner.Runner('Test')
            logging.info('Экземпляр класса Runner создан успешно', exc_info=True)
        except TypeError as er_T :
            logging.warning('Экземпляр класса Runner не создан, задано неверное имя', exc_info=True)
        for _ in range(1, 11):
            try:
                t_run.run()
                logging.info('"test_run" выполнен успешно', exc_info=True)
            except:
                logging.warning('Неверная скорость для Runner', exc_info=True)
        self.assertEqual(t_run.distance, 100)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode='w', filename = 'runner_test.log', format='%(asctime)s - %(levelname)s - %(message)s', encoding = 'UTF-8')
    unittest.main()
